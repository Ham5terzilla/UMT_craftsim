from abc import ABC, abstractmethod

from crafting_system.constants import ItemTypes, Machines, Tags
from crafting_system.dataclasses.items import Item
from crafting_system.service.mixins import TransformationHelperMixin


class Transformation_Multiple(ABC):
    @abstractmethod
    def transform(self, *components: Item) -> Item:
        pass


class FrameMakerTransformation(Transformation_Multiple):
    def transform(self, bar: Item, bolts: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(bar, ItemTypes.BAR)
        TransformationHelperMixin.validate_type(bolts, ItemTypes.BOLTS)

        totals = TransformationHelperMixin.properties_totals([bar, bolts])
        return Item(
            item_type=ItemTypes.FRAME,
            value=round(totals.value * 1.25),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.FRAME_MAKER],
        )


class RingMakerTransformation(Transformation_Multiple):
    def transform(self, gem: Item, coil: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(gem, ItemTypes.GEM)
        TransformationHelperMixin.validate_type(coil, ItemTypes.COIL)

        totals = TransformationHelperMixin.properties_totals([gem, coil])
        return Item(
            item_type=ItemTypes.RING,
            value=round(totals.value * 1.7),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.RING_MAKER],
        )


class BlastingPowderChamberTransformation(Transformation_Multiple):
    def transform(self, metal_dust: Item, stone_dust: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(metal_dust, "metal dust")
        TransformationHelperMixin.validate_type(stone_dust, "stone dust")

        totals = TransformationHelperMixin.properties_totals([metal_dust, stone_dust])
        return Item(
            item_type=ItemTypes.BLASTING_POWDER,
            value=2,
            materials=1,
            sequence=totals.sequence + [Machines.BLASTING_POWDER_CHAMBER],
        )


class ExplosivesMakerTransformation(Transformation_Multiple):
    def transform(self, blasting_powder: Item, casing_metal_or_ceramic: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(blasting_powder, ItemTypes.BLASTING_POWDER)
        TransformationHelperMixin.validate_multiple_items_types(
            [casing_metal_or_ceramic],
            [ItemTypes.METAL_CASING, ItemTypes.CERAMIC_CASING],
        )

        totals = TransformationHelperMixin.properties_totals(
            [blasting_powder, casing_metal_or_ceramic]
        )
        return Item(
            item_type=ItemTypes.EXPLOSIVES,
            value=round(casing_metal_or_ceramic.value * blasting_powder.value),
            materials=totals.materials,
            tags=casing_metal_or_ceramic.tags,
            sequence=totals.sequence + [Machines.EXPLOSIVES_MAKER],
        )


class CircuitMakerTransformation(Transformation_Multiple):
    def transform(self, glass: Item, coil: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(glass, ItemTypes.GLASS)
        TransformationHelperMixin.validate_type(coil, ItemTypes.COIL)

        totals = TransformationHelperMixin.properties_totals([glass, coil])
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


class CasingMachineTransformation(Transformation_Multiple):
    def transform(self, frame: Item, bolts: Item, plate: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(frame, ItemTypes.FRAME)
        TransformationHelperMixin.validate_type(bolts, ItemTypes.BOLTS)
        TransformationHelperMixin.validate_type(plate, ItemTypes.PLATE)

        totals = TransformationHelperMixin.properties_totals([frame, bolts, plate])
        return Item(
            item_type=ItemTypes.METAL_CASING,
            value=round(totals.value * 1.3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.CASING_MACHINE],
        )


class PrismaticGemCrucibleTransformation(Transformation_Multiple):
    def transform(self, gem1: Item, gem2: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_multiple_items_types([gem1, gem2], [ItemTypes.GEM])
        TransformationHelperMixin.validate_multiple_items_tags_absence(
            [gem1, gem2], [Tags.PRISMATIC]
        )

        totals = TransformationHelperMixin.properties_totals([gem1, gem2])
        return Item(
            item_type=ItemTypes.GEM,
            value=round(totals.value * 1.15),
            materials=totals.materials,
            tags=totals.tags + [Tags.PRISMATIC],
            sequence=totals.sequence + [Machines.PRISMATIC_GEM_CRUCIBLE],
        )


class AlloyFurnaceTransformation(Transformation_Multiple):
    def transform(self, bar1: Item, bar2: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_multiple_items_types([bar1, bar2], [ItemTypes.BAR])
        TransformationHelperMixin.validate_multiple_items_tags_absence([bar1, bar2], [Tags.ALLOYED])

        totals = TransformationHelperMixin.properties_totals([bar1, bar2])
        return Item(
            item_type=ItemTypes.BAR,
            value=round(totals.value * 1.2),
            materials=totals.materials,
            tags=totals.tags + [Tags.ALLOYED],
            sequence=totals.sequence + [Machines.ALLOY_FURNACE],
        )


class MagneticMachineTransformation(Transformation_Multiple):
    def transform(self, coil: Item, metal_casing: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(coil, ItemTypes.COIL)
        TransformationHelperMixin.validate_type(metal_casing, ItemTypes.METAL_CASING)

        totals = TransformationHelperMixin.properties_totals([coil, metal_casing])
        return Item(
            item_type=ItemTypes.ELECTROMAGNET,
            value=round(totals.value * 1.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.MAGNETIC_MACHINE],
        )


class OpticsMachineTransformation(Transformation_Multiple):
    def transform(self, lens: Item, pipe: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(lens, ItemTypes.LENS)
        TransformationHelperMixin.validate_type(pipe, ItemTypes.PIPE)

        totals = TransformationHelperMixin.properties_totals([lens, pipe])
        return Item(
            item_type=ItemTypes.OPTICS,
            value=round(totals.value * 1.25),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.OPTICS_MACHINE],
        )


class GilderTransformation(Transformation_Multiple):
    def transform(self, filigree: Item, jewellery: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(filigree, ItemTypes.FILIGREE)
        TransformationHelperMixin.validate_multiple_items_types(
            [jewellery], [ItemTypes.RING, ItemTypes.AMULET]
        )
        TransformationHelperMixin.validate_tag_absence(jewellery, Tags.GILDED)

        totals = TransformationHelperMixin.properties_totals([filigree, jewellery])
        return Item(
            item_type=jewellery.item_type,
            value=round(totals.value * 1.2),
            materials=totals.materials,
            tags=totals.tags + [Tags.GILDED],
            sequence=totals.sequence + [Machines.GILDER],
        )


class EngineFactoryTransformation(Transformation_Multiple):
    def transform(self, mechanical_parts: Item, pipe: Item, metal_casing: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(mechanical_parts, ItemTypes.MECHANICAL_PARTS)
        TransformationHelperMixin.validate_type(pipe, ItemTypes.PIPE)
        TransformationHelperMixin.validate_type(metal_casing, ItemTypes.METAL_CASING)

        totals = TransformationHelperMixin.properties_totals([mechanical_parts, pipe, metal_casing])
        return Item(
            item_type=ItemTypes.ENGINE,
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.ENGINE_FACTORY],
        )


class SuperconductorConstructorTransformation(Transformation_Multiple):
    def transform(self, alloyed_bar: Item, ceramic_casing: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(alloyed_bar, ItemTypes.BAR)
        TransformationHelperMixin.validate_tag_present(alloyed_bar, Tags.ALLOYED)
        TransformationHelperMixin.validate_type(ceramic_casing, ItemTypes.CERAMIC_CASING)

        totals = TransformationHelperMixin.properties_totals([alloyed_bar, ceramic_casing])
        return Item(
            item_type=ItemTypes.SUPERCONDUCTOR,
            value=round(totals.value * 3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.SUPERCONDUCTOR_CONSTRUCTOR],
        )


class AmuletMakerTransformation(Transformation_Multiple):
    def transform(self, ring: Item, frame: Item, prismatic_gem: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(ring, ItemTypes.RING)
        TransformationHelperMixin.validate_type(frame, ItemTypes.FRAME)
        TransformationHelperMixin.validate_type(prismatic_gem, ItemTypes.GEM)
        TransformationHelperMixin.validate_tag_present(prismatic_gem, Tags.PRISMATIC)

        totals = TransformationHelperMixin.properties_totals([ring, frame, prismatic_gem])
        return Item(
            item_type=ItemTypes.AMULET,
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.AMULET_MAKER],
        )


class TabletFactoryTransformation(Transformation_Multiple):
    def transform(self, metal_casing: Item, glass: Item, circuit: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(metal_casing, ItemTypes.METAL_CASING)
        TransformationHelperMixin.validate_type(glass, ItemTypes.GLASS)
        TransformationHelperMixin.validate_type(circuit, ItemTypes.CIRCUIT)

        totals = TransformationHelperMixin.properties_totals([metal_casing, glass, circuit])
        return Item(
            item_type=ItemTypes.TABLET,
            value=round(totals.value * 3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.TABLET_FACTORY],
        )


class BlastingPowderRefinerTransformation(Transformation_Multiple):
    """Bruh, just skip this bullshit until later, if really need make Item(item_type=ItemTypes.BLASTING_POWDER, value=2, materials=2) or materials = 0 or whatever you want"""

    pass


class LaserMakerTransformation(Transformation_Multiple):
    def transform(self, optics: Item, gem: Item, circuit: Item) -> Item:  # type: ignore
        TransformationHelperMixin.validate_type(optics, ItemTypes.OPTICS)
        TransformationHelperMixin.validate_type(gem, ItemTypes.GEM)
        TransformationHelperMixin.validate_type(circuit, ItemTypes.CIRCUIT)

        totals = TransformationHelperMixin.properties_totals([optics, gem, circuit])
        return Item(
            item_type=ItemTypes.LASER,
            value=round(totals.value * 2.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + [Machines.LASER_MAKER],
        )


class PowerCoreAssemblerTransformation(Transformation_Multiple):
    def transform(  # type: ignore
        self, metal_casing: Item, superconductor: Item, electromagnet: Item
    ) -> Item:
        TransformationHelperMixin.validate_type(metal_casing, ItemTypes.METAL_CASING)
        TransformationHelperMixin.validate_type(superconductor, ItemTypes.SUPERCONDUCTOR)
        TransformationHelperMixin.validate_type(electromagnet, ItemTypes.ELECTROMAGNET)

        totals = TransformationHelperMixin.properties_totals(
            [metal_casing, superconductor, electromagnet]
        )
        return Item(
            item_type=ItemTypes.POWER_CORE,
            value=round(totals.value * 2.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Power Core Assembler"],
        )
