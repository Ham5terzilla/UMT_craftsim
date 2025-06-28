from dataclasses import dataclass, field
from typing import List

from crafting_system import constants
from crafting_system.service.exceptions import ItemValidationError


@dataclass
class Item:
    item_type: str = constants.ItemTypes.UNKNOWN
    value: int = 0
    materials: float = 1.0
    dustwork_type: str = constants.DustTypes.UNKNOWN
    tags: list[str] = field(default_factory=list)
    sequence: list[str] | List = field(default_factory=list)

    def __post_init__(self):
        if self.materials < 0:
            raise ItemValidationError("Materials cannot be negative", self)

    @property
    def value_per_materials(self) -> float:
        return self.value / self.materials if self.materials else 0

    def short_sequence(self) -> str:
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

    def __str__(self):
        shorter_seq = "no sequence"
        if self.sequence:
            shorter_seq = self.sequence[-1]
        return (
            f"{self.item_type:16} | Val: {self.value:8} | Mats: {self.materials:4.1f} | "
            f"VPM: {self.value_per_materials:11.2f} | {shorter_seq}"
        )

    def table_full(self) -> str:
        return (
            f"{self.item_type:16} | Val: {self.value:8} | Mats: {self.materials:4.1f} | "
            f"VPM: {self.value_per_materials:11.2f} | {self.short_sequence()}"
        )

    @classmethod
    def create_ore(cls, predefined_ore_name: str):
        item_type = "ore"
        value = 0
        match predefined_ore_name:
            case "Tin":
                value = 10
            case "Iron":
                value = 20
            case "Lead":
                value = 30
            case "Cobalt":
                value = 50
            case "Aluminium":
                value = 65
            case "Silver":
                value = 150
            case "Uranium":
                value = 180
            case "Vanadium":
                value = 240
            case "Tungsten":
                value = 300
            case "Gold":
                value = 350
            case "Titanium":
                value = 400
            case "Molybdenum":
                value = 600
            case "Plutonium":
                value = 1000
            case "Mithril":
                value = 2000
            case "Thorium":
                value = 3200
            case "Iridium":
                value = 3700
            case "Adamantium":
                value = 4500
            case "Rhodium":
                value = 15000
            case "Unobtainium":
                value = 30000
            case _:
                raise Exception(f"Ore with name {predefined_ore_name} does not exist")
        return cls(item_type=item_type, value=value)

    @classmethod
    def create_gem(cls, predefined_gem_name: str):
        item_type = "gem"
        value = 0
        match predefined_gem_name:
            case "Topaz":
                value = 65
            case "Emerald":
                value = 200
            case "Sapphire":
                value = 250
            case "Ruby":
                value = 300
            case "Diamond":
                value = 1500
            case "Poudretteite":
                value = 1700
            case "Zultanite":
                value = 2300
            case "Gradidierite":
                value = 4500
            case "Musgravite":
                value = 5800
            case "Painite":
                value = 12000
            case _:
                raise Exception(f"Gem with name {predefined_gem_name} does not exist")
        return cls(item_type=item_type, value=value)
