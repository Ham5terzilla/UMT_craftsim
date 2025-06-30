"""
Core item representation for a crafting system.\n
Defines the Item dataclass that serves as the fundamental building block\n
for all craftable entities in the system.\n
Each Item tracks:\n
- Core properties (type, value, material cost)\n
- Processing history (tags, sequence)
"""

from dataclasses import dataclass, field

from umt_craftsim import constants
from umt_craftsim.service.exceptions import ItemValidationError


@dataclass
class Item:
    """Represents a item with processing history, tags, etc.\n
    Attributes:
        item_type (str): type of item, better to use ItemTypes constants. Defaults to "unknown"
        value (int): Monetary worth. Defaults to 0.
        materials (float): Resource units consumed for creation, both, ores and gems. Defaults to 1.0.
        tags (list[str]): Applied tags (Cleaned, Alloyed etc), better to use Tags constants. Defaults to empty list.
        sequence (list[str] | list): Crafting steps (machines), better to use Machines constants. Defaults to empty list.
        value_per_materials (float): value devided by materials, automatically generated after every update of value or materials.
        dustwork_type (str): type of dust of item after crushing item or when item_type is dust already. Defaults to "unknown".
    """

    item_type: str = constants.ItemTypes.UNKNOWN.value
    value: int = 0
    materials: float = 1.0
    dustwork_type: str = constants.DustTypes.UNKNOWN.value
    tags: list[str] = field(default_factory=list)
    sequence: list[str] | list = field(default_factory=list)

    def __post_init__(self):
        """Validates item properties after initialization.

        Raises:
            ItemValidationError: if materials value is negative
        """
        if self.materials < 0:
            raise ItemValidationError("Materials cannot be negative", self)

    @property
    def value_per_materials(self) -> float:
        """Calculates value efficiency per material unit.

        Returns:
            float: value/materials ratio, or 0 if materials = 0
        """
        return self.value / self.materials if self.materials != 0 else 0

    def short_sequence(self) -> str:
        """Compress crafting sequence into compact str representation.\n
        Processes sequence in reverse order, showing only the final steps of nested sequence.

        Returns:
            str: Compact sequence represenation or "no sequence"
        """
        short_seq = "no sequence"
        if self.sequence:
            short_seq = ""
            for i in range(len(self.sequence)):
                part = ""
                if isinstance(self.sequence[i], list):
                    part = f"{self.sequence[i][-1]} + "
                else:
                    part = f"{self.sequence[i]} <-|"
                short_seq = part + short_seq
            while not short_seq[-1].isalnum():
                short_seq = short_seq[:-1]
        return short_seq

    def __str__(self) -> str:
        """Standart string represenation showing key properties.\n
        Format:\n
        [item_type] | Val: [value] | Mats: [materials] | VPM: [value_per_materials] | [last_step]

        Returns:
            str: Formatted single-line summary
        """
        shorter_seq = "no sequence"
        if self.sequence:
            shorter_seq = self.sequence[-1]
        return (
            f"{self.item_type:16} | Val: {self.value:8} | Mats: {self.materials:4.1f} | "
            f"VPM: {self.value_per_materials:11.2f} | {shorter_seq}"
        )

    def table_full(self) -> str:
        """Detailed string representation including compressed sequence.\n
        Format:\n
        [item_type] | Val: [value] | Mats: [materials] | VPM: [value_per_materials] | [short_sequence]

        Returns:
            str: Formatted single-line summary
        """
        return (
            f"{self.item_type:16} | Val: {self.value:8} | Mats: {self.materials:4.1f} | "
            f"VPM: {self.value_per_materials:11.2f} | {self.short_sequence()}"
        )
