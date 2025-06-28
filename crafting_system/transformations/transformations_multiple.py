from abc import ABC, abstractmethod

from crafting_system.constants import ItemTypes, Machines, Tags
from crafting_system.dataclasses.items import Item
from crafting_system.service.mixins import TransformationHelperMixin


class Transformation_Multiple(ABC):
    @abstractmethod
    def transform(self, *components: Item) -> Item:
        pass


class FrameMakerTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, bar: Item, bolts: Item) -> Item:  # type: ignore
        self.validate_type(bar, ItemTypes.BAR)
        self.validate_type(bolts, ItemTypes.BOLTS)

        totals = self.properties_totals([bar, bolts])
        return Item(
            item_type=ItemTypes.FRAME,
            value=round(totals.value * 1.25),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.FRAME_MAKER],
        )


class RingMakerTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, gem: Item, coil: Item) -> Item:  # type: ignore
        self.validate_type(gem, ItemTypes.GEM)
        self.validate_type(coil, ItemTypes.COIL)

        totals = self.properties_totals([gem, coil])
        return Item(
            item_type=ItemTypes.RING,
            value=round(totals.value * 1.7),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.RING_MAKER],
        )


class BlastingPowderChamberTransformation(
    Transformation_Multiple, TransformationHelperMixin
):
    def transform(self, metal_dust: Item, stone_dust: Item) -> Item:  # type: ignore
        self.validate_type(metal_dust, "metal dust")
        self.validate_type(stone_dust, "stone dust")

        totals = self.properties_totals([metal_dust, stone_dust])
        return Item(
            item_type=ItemTypes.BLASTING_POWDER,
            value=2,
            materials=1,
            sequence=totals.sequence + [Machines.BLASTING_POWDER_CHAMBER],
        )


class ExplosivesMakerTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, blasting_powder: Item, casing_metal_or_ceramic: Item) -> Item:  # type: ignore
        self.validate_type(blasting_powder, ItemTypes.BLASTING_POWDER)
        self.validate_multiple_items_types(
            [casing_metal_or_ceramic],
            [ItemTypes.METAL_CASING, ItemTypes.CERAMIC_CASING],
        )

        totals = self.properties_totals([blasting_powder, casing_metal_or_ceramic])
        return Item(
            item_type=ItemTypes.EXPLOSIVES,
            value=round(casing_metal_or_ceramic.value * blasting_powder.value),
            materials=totals.materials,
            tags=casing_metal_or_ceramic.tags,
            sequence=totals.sequence + [Machines.EXPLOSIVES_MAKER],
        )


class CircuitMakerTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, glass: Item, coil: Item) -> Item:  # type: ignore
        self.validate_type(glass, ItemTypes.GLASS)
        self.validate_type(coil, ItemTypes.COIL)

        totals = self.properties_totals([glass, coil])
        return Item(
            item_type=ItemTypes.CIRCUIT,
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.CIRCUIT_MAKER],
        )


class ClayMixerTransformation:
    """dusts are stupid, use for dust related operations direct creation of predefined types items in Items.create_[something]
    might implement dust-related things after full 100% accurate implementation of Crusher, or who even cares about dusts outside of siefting"""

    pass


class CasingMachineTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, frame: Item, bolts: Item, plate: Item) -> Item:  # type: ignore
        self.validate_type(frame, ItemTypes.FRAME)
        self.validate_type(bolts, ItemTypes.BOLTS)
        self.validate_type(plate, ItemTypes.PLATE)

        totals = self.properties_totals([frame, bolts, plate])
        return Item(
            item_type=ItemTypes.METAL_CASING,
            value=round(totals.value * 1.3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.CASING_MACHINE],
        )


class PrismaticGemCrucibleTransformation(
    Transformation_Multiple, TransformationHelperMixin
):
    def transform(self, gem1: Item, gem2: Item) -> Item:  # type: ignore
        self.validate_multiple_items_types([gem1, gem2], [ItemTypes.GEM])
        self.validate_multiple_items_tags_absence([gem1, gem2], [Tags.PRISMATIC])

        totals = self.properties_totals([gem1, gem2])
        return Item(
            item_type=ItemTypes.GEM,
            value=round(totals.value * 1.15),
            materials=totals.materials,
            tags=totals.tags + [Tags.PRISMATIC],
            sequence=totals.sequence + [Machines.PRISMATIC_GEM_CRUCIBLE],
        )


class AlloyFurnaceTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, bar1: Item, bar2: Item) -> Item:  # type: ignore
        self.validate_multiple_items_types([bar1, bar2], [ItemTypes.BAR])
        self.validate_multiple_items_tags_absence([bar1, bar2], [Tags.ALLOYED])

        totals = self.properties_totals([bar1, bar2])
        return Item(
            item_type=ItemTypes.BAR,
            value=round(totals.value * 1.2),
            materials=totals.materials,
            tags=totals.tags + [Tags.ALLOYED],
            sequence=totals.sequence + [Machines.ALLOY_FURNACE],
        )


class MagneticMachineTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, coil: Item, metal_casing: Item) -> Item:  # type: ignore
        self.validate_type(coil, ItemTypes.COIL)
        self.validate_type(metal_casing, ItemTypes.METAL_CASING)

        totals = self.properties_totals([coil, metal_casing])
        return Item(
            item_type=ItemTypes.ELECTROMAGNET,
            value=round(totals.value * 1.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.MAGNETIC_MACHINE],
        )


class OpticsMachineTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, lens: Item, pipe: Item) -> Item:  # type: ignore
        self.validate_type(lens, ItemTypes.LENS)
        self.validate_type(pipe, ItemTypes.PIPE)

        totals = self.properties_totals([lens, pipe])
        return Item(
            item_type=ItemTypes.OPTICS,
            value=round(totals.value * 1.25),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.OPTICS_MACHINE],
        )


class GilderTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, filigree: Item, jewellery: Item) -> Item:  # type: ignore
        self.validate_type(filigree, ItemTypes.FILIGREE)
        self.validate_multiple_items_types(
            [jewellery], [ItemTypes.RING, ItemTypes.AMULET]
        )
        self.validate_tag_absence(jewellery, Tags.GILDED)

        totals = self.properties_totals([filigree, jewellery])
        return Item(
            item_type=jewellery.item_type,
            value=round(totals.value * 1.2),
            materials=totals.materials,
            tags=totals.tags + [Tags.GILDED],
            sequence=totals.sequence + [Machines.GILDER],
        )


class EngineFactoryTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, mechanical_parts: Item, pipe: Item, metal_casing: Item) -> Item:  # type: ignore
        self.validate_type(mechanical_parts, ItemTypes.MECHANICAL_PARTS)
        self.validate_type(pipe, ItemTypes.PIPE)
        self.validate_type(metal_casing, ItemTypes.METAL_CASING)

        totals = self.properties_totals([mechanical_parts, pipe, metal_casing])
        return Item(
            item_type=ItemTypes.ENGINE,
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.ENGINE_FACTORY],
        )


class SuperconductorConstructorTransformation(
    Transformation_Multiple, TransformationHelperMixin
):
    def transform(self, alloyed_bar: Item, ceramic_casing: Item) -> Item:  # type: ignore
        self.validate_type(alloyed_bar, ItemTypes.BAR)
        self.validate_tag_present(alloyed_bar, Tags.ALLOYED)
        self.validate_type(ceramic_casing, ItemTypes.CERAMIC_CASING)

        totals = self.properties_totals([alloyed_bar, ceramic_casing])
        return Item(
            item_type=ItemTypes.SUPERCONDUCTOR,
            value=round(totals.value * 3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.SUPERCONDUCTOR_CONSTRUCTOR],
        )


class AmuletMakerTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, ring: Item, frame: Item, prismatic_gem: Item) -> Item:  # type: ignore
        self.validate_type(ring, ItemTypes.RING)
        self.validate_type(frame, ItemTypes.FRAME)
        self.validate_type(prismatic_gem, ItemTypes.GEM)
        self.validate_tag_present(prismatic_gem, Tags.PRISMATIC)

        totals = self.properties_totals([ring, frame, prismatic_gem])
        return Item(
            item_type=ItemTypes.AMULET,
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.AMULET_MAKER],
        )


class TabletFactoryTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, metal_casing: Item, glass: Item, circuit: Item) -> Item:  # type: ignore
        self.validate_type(metal_casing, ItemTypes.METAL_CASING)
        self.validate_type(glass, ItemTypes.GLASS)
        self.validate_type(circuit, ItemTypes.CIRCUIT)

        totals = self.properties_totals([metal_casing, glass, circuit])
        return Item(
            item_type=ItemTypes.TABLET,
            value=round(totals.value * 3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.TABLET_FACTORY],
        )


class BlastingPowderRefinerTransformation(
    Transformation_Multiple, TransformationHelperMixin
):
    """Bruh, just skip this bullshit until later, if really need make Item(item_type=ItemTypes.BLASTING_POWDER, value=2, materials=2) or materials = 0 or whatever you want"""

    pass


class LaserMakerTransformation(Transformation_Multiple, TransformationHelperMixin):
    def transform(self, optics: Item, gem: Item, circuit: Item) -> Item:  # type: ignore
        self.validate_type(optics, ItemTypes.OPTICS)
        self.validate_type(gem, ItemTypes.GEM)
        self.validate_type(circuit, ItemTypes.CIRCUIT)

        totals = self.properties_totals([optics, gem, circuit])
        return Item(
            item_type=ItemTypes.LASER,
            value=round(totals.value * 2.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.LASER_MAKER],
        )


class PowerCoreAssemblerTransformation(
    Transformation_Multiple, TransformationHelperMixin
):
    def transform(  # type: ignore
        self, metal_casing: Item, superconductor: Item, electromagnet: Item
    ) -> Item:
        self.validate_type(metal_casing, ItemTypes.METAL_CASING)
        self.validate_type(superconductor, ItemTypes.SUPERCONDUCTOR)
        self.validate_type(electromagnet, ItemTypes.ELECTROMAGNET)

        totals = self.properties_totals([metal_casing, superconductor, electromagnet])
        return Item(
            item_type=ItemTypes.POWER_CORE,
            value=round(totals.value * 2.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Power Core Assembler"],
        )
