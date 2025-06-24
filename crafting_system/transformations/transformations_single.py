from abc import ABC, abstractmethod

from crafting_system.dataclasses.items import Item
from crafting_system.mixins import ValidationMixin


class Transformation_Single(ABC):
    @abstractmethod
    def transform(self, item: Item) -> Item:
        pass


class OreCleanerTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "ore")
        self.validate_tag_absence(item, "Cleaned")

        return Item(
            item_type=item.item_type,
            value=item.value + 10,
            materials=item.materials,
            tags=item.tags + ["Cleaned"],
            sequence=item.sequence + ["Ore Cleaner"],
        )


class PolisherTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_tag_absence(item, "Polished")

        return Item(
            item_type=item.item_type,
            value=item.value + 10,
            materials=item.materials,
            tags=item.tags + ["Polished"],
            sequence=item.sequence + ["Polisher"],
        )


class OreSmelterTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "ore")

        return Item(
            item_type="bar",
            value=round(item.value * 1.2),
            materials=item.materials,
            tags=item.tags + ["Smelted"],
            sequence=item.sequence + ["Ore Smelter"],
        )


class CoilerTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "bar")

        return Item(
            item_type="coil",
            value=item.value + 20,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Coiler"],
        )


class BoltMachineTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "bar")

        return Item(
            item_type="bolts",
            value=item.value + 5,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Bolt Machine"],
        )


class PlateStamperTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "bar")

        return Item(
            item_type="plate",
            value=item.value + 20,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Plate Stamper"],
        )


class PipeMakerTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "plate")

        return Item(
            item_type="pipe",
            value=item.value + 20,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Pipe Maker"],
        )


class MechanicalPartsMakerTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "plate")

        return Item(
            item_type="mechanical parts",
            value=item.value + 30,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Mechanical Parts Maker"],
        )


class ElectronicTunerTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_tag_absence(item, "Tuned")
        self.validate_tag_present(item, "Electronics")

        return Item(
            item_type=item.item_type,
            value=item.value + 50,
            materials=item.materials,
            tags=item.tags + ["Tuned"],
            sequence=item.sequence + ["Electronic Tuner"],
        )


class GemCutterTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "gem")
        self.validate_tag_absence(item, "Cut")

        return Item(
            item_type=item.item_type,
            value=round(item.value * 1.4),
            materials=item.materials,
            tags=item.tags + ["Cut"],
            sequence=item.sequence + ["Gem Cutter"],
        )


class BlastFurnaceTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "ore")

        return Item(
            item_type="bar",
            value=round(item.value * 0.8),
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Blast Furnace"],
        )


class CeremicFurnaceTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "clay block")

        return Item(
            item_type="ceramic casing",
            value=150,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Ceramic Furnace"],
        )


class TemperingForgeTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "bar")
        self.validate_tag_absence(item, "Tempered")

        return Item(
            item_type=item.item_type,
            value=round(item.value * 2),
            materials=item.materials,
            tags=item.tags + ["Tempered"],
            sequence=item.sequence + ["Tempering Forge"],
        )


class FiligreeCutterTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "plate")

        return Item(
            item_type="filigree",
            value=round(item.value * 1.1),
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Filigree Cutter"],
        )


class LensCutterTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "glass")

        return Item(
            item_type="lens",
            value=item.value + 50,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Lens Cutter"],
        )


class QAMachineTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_tag_absence(item, "Quality Assured")

        return Item(
            item_type=item.item_type,
            value=round(item.value * 1.2),
            materials=item.materials,
            tags=item.tags + ["Quality Assured"],
            sequence=item.sequence + ["Quality Assurance Machine"],
        )


class DuplicatorTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_tag_absence(item, "Duplicated")

        return Item(
            item_type=item.item_type,
            value=round(item.value * 0.5),
            materials=item.materials * 0.5,
            tags=item.tags + ["Duplicated"],
            sequence=item.sequence + ["Duplicated"],
        )


class PhilosophersStoneTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "ore")
        self.validate_tag_absence(item, "Gold Infused")

        return Item(
            item_type=item.item_type,
            value=round(item.value * 1.25),
            materials=item.materials,
            tags=item.tags + ["Gold Infused"],
            sequence=item.sequence + ["Philosophers Stone"],
        )


class OreUpgraderTransformation(Transformation_Single, ValidationMixin):
    """Just don't use this after anything, might update later"""

    def transform(self, item: Item) -> Item:
        self.validate_type(item, "ore")
        if item.tags:
            raise Exception("DUDE, STOP, DON'T USE ORE UPGRADER AFTER ANYTHING")

        value = item.value
        ores = [10, 20, 30, 50, 65, 150, 180, 240, 300, 350, 400, 600, 1000, 1200, 2000]
        value = ores[ores.index(value) + 1]
        return Item(
            item_type=item.item_type,
            value=value,
            materials=item.materials,
            tags=item.tags + ["Upgraded"],
            sequence=item.sequence + ["Ore Upgrader"],
        )


class GTBTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "gem")

        return Item(
            item_type="bar",
            value=item.value,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Gem To Bar Transmuter"],
        )


class BTGTransformation(Transformation_Single, ValidationMixin):
    def transform(self, item: Item) -> Item:
        self.validate_type(item, "bar")

        return Item(
            item_type="gem",
            value=item.value,
            materials=item.materials,
            tags=item.tags,
            sequence=item.sequence + ["Bar To Gem Transmuter"],
        )
