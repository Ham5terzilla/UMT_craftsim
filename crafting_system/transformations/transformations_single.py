from abc import ABC, abstractmethod

from crafting_system.constants import ItemTypes, Machines, Tags
from crafting_system.dataclasses.items import Item
from crafting_system.service.mixins import TransformationHelperMixin


class Transformation_Single(ABC):
    @abstractmethod
    def transform(self, item: Item) -> Item:
        pass


# Reason why type: ignore everywhere is to surpess mismatch of names of vars of realization of transform
class OreCleanerTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, ore: Item) -> Item:  # type: ignore
        self.validate_type(ore, ItemTypes.ORE)
        self.validate_tag_absence(ore, Tags.CLEANED)

        return Item(
            item_type=ore.item_type,
            value=ore.value + 10,
            materials=ore.materials,
            tags=ore.tags + [Tags.CLEANED],
            sequence=ore.sequence + [Machines.ORE_CLEANER],
        )


class PolisherTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, any_item: Item) -> Item:  # type: ignore
        self.validate_tag_absence(any_item, Tags.POLISHED)

        return Item(
            item_type=any_item.item_type,
            value=any_item.value + 10,
            materials=any_item.materials,
            tags=any_item.tags + [Tags.POLISHED],
            sequence=any_item.sequence + [Machines.POLISHER],
        )


class OreSmelterTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, ore: Item) -> Item:  # type: ignore
        self.validate_type(ore, ItemTypes.ORE)

        return Item(
            item_type=ItemTypes.BAR,
            value=round(ore.value * 1.2),
            materials=ore.materials,
            tags=ore.tags + [Tags.SMELTED],
            sequence=ore.sequence + [Machines.ORE_SMELTER],
        )


class CoilerTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, bar: Item) -> Item:  # type: ignore
        self.validate_type(bar, ItemTypes.BAR)

        return Item(
            item_type=ItemTypes.COIL,
            value=bar.value + 20,
            materials=bar.materials,
            tags=bar.tags + [Tags.DRAWN],
            sequence=bar.sequence + [Machines.COILER],
        )


class BoltMachineTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, bar: Item) -> Item:  # type: ignore
        self.validate_type(bar, ItemTypes.BAR)

        return Item(
            item_type=ItemTypes.BOLTS,
            value=bar.value + 5,
            materials=bar.materials,
            tags=bar.tags + [Tags.BOLTS],
            sequence=bar.sequence + [Machines.BOLT_MACHINE],
        )


class PlateStamperTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, bar: Item) -> Item:  # type: ignore
        self.validate_type(bar, ItemTypes.BAR)

        return Item(
            item_type=ItemTypes.PLATE,
            value=bar.value + 20,
            materials=bar.materials,
            tags=bar.tags + [Tags.PLATE],
            sequence=bar.sequence + [Machines.PLATE_STAMPER],
        )


class PipeMakerTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, plate: Item) -> Item:  # type: ignore
        self.validate_type(plate, ItemTypes.PLATE)

        return Item(
            item_type=ItemTypes.PIPE,
            value=plate.value + 20,
            materials=plate.materials,
            tags=plate.tags + [Tags.PIPE],
            sequence=plate.sequence + [Machines.PIPE_MAKER],
        )


class MechanicalPartsMakerTransformation(
    Transformation_Single, TransformationHelperMixin
):
    def transform(self, plate: Item) -> Item:  # type: ignore
        self.validate_type(plate, ItemTypes.PLATE)

        return Item(
            item_type=ItemTypes.MECHANICAL_PARTS,
            value=plate.value + 30,
            materials=plate.materials,
            tags=plate.tags + [Tags.MECHANICAL_PARTS],
            sequence=plate.sequence + [Machines.MECHANICAL_PARTS_MAKER],
        )


class ElectronicTunerTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, electronics: Item) -> Item:  # type: ignore
        self.validate_tag_absence(electronics, Tags.TUNED)
        self.validate_multiple_items_types(
            [electronics],
            [
                ItemTypes.CIRCUIT,
                ItemTypes.ELECTROMAGNET,
                ItemTypes.TABLET,
                ItemTypes.POWER_CORE,
            ],
        )

        return Item(
            item_type=electronics.item_type,
            value=electronics.value + 50,
            materials=electronics.materials,
            tags=electronics.tags + [Tags.TUNED],
            sequence=electronics.sequence + [Machines.ELECTRONIC_TUNER],
        )


class GemCutterTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, gem: Item) -> Item:  # type: ignore
        self.validate_type(gem, ItemTypes.GEM)
        self.validate_tag_absence(gem, Tags.CUT)

        return Item(
            item_type=gem.item_type,
            value=round(gem.value * 1.4),
            materials=gem.materials,
            tags=gem.tags + [Tags.CUT],
            sequence=gem.sequence + [Machines.GEM_CUTTER],
        )


class BlastFurnaceTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, ore: Item) -> Item:  # type: ignore
        self.validate_type(ore, ItemTypes.ORE)

        return Item(
            item_type=ItemTypes.BAR,
            value=round(ore.value * 0.8),
            materials=ore.materials,
            tags=ore.tags + [Tags.SMELTED],
            sequence=ore.sequence + [Machines.BLAST_FURNACE],
        )


class CeramicFurnaceTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, clay_block: Item) -> Item:  # type: ignore
        self.validate_type(clay_block, ItemTypes.CLAY_BLOCK)

        return Item(
            item_type=ItemTypes.CERAMIC_CASING,
            value=150,
            materials=clay_block.materials,
            tags=clay_block.tags + [Tags.CERAMIC],
            sequence=clay_block.sequence + [Machines.CERAMIC_FURNACE],
        )


class TemperingForgeTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, bar: Item) -> Item:  # type: ignore
        self.validate_type(bar, ItemTypes.BAR)
        self.validate_tag_absence(bar, Tags.TEMPERED)

        return Item(
            item_type=bar.item_type,
            value=round(bar.value * 2),
            materials=bar.materials,
            tags=bar.tags + [Tags.TEMPERED],
            sequence=bar.sequence + [Machines.TEMPERING_FORGE],
        )


class FiligreeCutterTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, plate: Item) -> Item:  # type: ignore
        self.validate_type(plate, ItemTypes.PLATE)

        return Item(
            item_type=ItemTypes.FILIGREE,
            value=round(plate.value * 1.1),
            materials=plate.materials,
            tags=plate.tags + [Tags.FILIGREE],
            sequence=plate.sequence + ["Filigree Cutter"],
        )


class LensCutterTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, glass: Item) -> Item:  # type: ignore
        self.validate_type(glass, ItemTypes.GLASS)

        return Item(
            item_type=ItemTypes.LENS,
            value=glass.value + 50,
            materials=glass.materials,
            tags=glass.tags,  # I tested, here is no tag in game for some reason
            sequence=glass.sequence + [Machines.LENS_CUTTER],
        )


class QAMachineTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, any_item: Item) -> Item:  # type: ignore
        self.validate_tag_absence(any_item, Tags.QUALITY_ASSURED)

        return Item(
            item_type=any_item.item_type,
            value=round(any_item.value * 1.2),
            materials=any_item.materials,
            tags=any_item.tags + [Tags.QUALITY_ASSURED],
            sequence=any_item.sequence + [Machines.QUALITY_ASSURANCE_MACHINE],
        )


class DuplicatorTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, any_item: Item) -> Item:  # type: ignore
        self.validate_tag_absence(any_item, Tags.DUPLICATED)

        return Item(
            item_type=any_item.item_type,
            value=round(any_item.value * 0.5),
            materials=any_item.materials * 0.5,
            tags=any_item.tags + [Tags.DUPLICATED],
            sequence=any_item.sequence + [Machines.DUPLICATOR],
        )


class PhilosophersStoneTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, ore: Item) -> Item:  # type: ignore
        self.validate_type(ore, ItemTypes.ORE)
        self.validate_tag_absence(ore, Tags.GOLD_INFUSED)

        return Item(
            item_type=ore.item_type,
            value=round(ore.value * 1.25),
            materials=ore.materials,
            tags=ore.tags + [Tags.GOLD_INFUSED],
            sequence=ore.sequence + [Machines.PHILOSOPHERS_STONE],
        )


class OreUpgraderTransformation(Transformation_Single, TransformationHelperMixin):
    """Just don't use this after anything, might update later"""

    def transform(self, ore: Item) -> Item:  # type: ignore
        self.validate_type(ore, ItemTypes.ORE)
        if ore.tags:
            raise Exception("DUDE, STOP, DON'T USE ORE UPGRADER AFTER ANYTHING")

        value = ore.value
        ores = [10, 20, 30, 50, 65, 150, 180, 240, 300, 350, 400, 600, 1000, 1200, 2000]
        value = ores[ores.index(value) + 1]
        return Item(
            item_type=ore.item_type,
            value=value,
            materials=ore.materials,
            tags=ore.tags + [Tags.UPGRADED],
            sequence=ore.sequence + [Machines.ORE_UPGRADER],
        )


class GTBTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, gem: Item) -> Item:  # type: ignore
        self.validate_type(gem, ItemTypes.GEM)

        return Item(
            item_type=ItemTypes.BAR,
            value=gem.value,
            materials=gem.materials,
            tags=gem.tags,
            sequence=gem.sequence + [Machines.GEM_TO_BAR_TRANSMUTER],
        )


class BTGTransformation(Transformation_Single, TransformationHelperMixin):
    def transform(self, bar: Item) -> Item:  # type: ignore
        self.validate_type(bar, ItemTypes.BAR)

        return Item(
            item_type=ItemTypes.GEM,
            value=bar.value,
            materials=bar.materials,
            tags=bar.tags,
            sequence=bar.sequence + [Machines.BAR_TO_GEM_TRANSMUTER],
        )


class CrusherTransformation(Transformation_Single, TransformationHelperMixin):
    """
    Actually the worst machine in game.\n
    Dusts are very incosistent with barely documentation in game neither researches from community.
    """

    pass
