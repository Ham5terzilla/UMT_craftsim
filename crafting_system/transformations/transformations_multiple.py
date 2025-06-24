from abc import ABC, abstractmethod

from crafting_system.dataclasses.items import Item
from crafting_system.mixins import TransformationHelperMixin, ValidationMixin


class Transformation_Multiple(ABC):
    @abstractmethod
    def transform(self, *components: Item) -> Item:
        pass


class FrameMakerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, bar: Item, bolts: Item) -> Item:  # type: ignore
        self.validate_type(bar, "bar")
        self.validate_type(bolts, "bolts")

        totals = self.properties_totals([bar, bolts])
        return Item(
            item_type="metal frame",
            value=round(totals.value * 1.25),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Frame Maker"],
        )


class RingMakerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, gem: Item, coil: Item) -> Item:  # type: ignore
        self.validate_type(gem, "gem")
        self.validate_type(coil, "coil")

        totals = self.properties_totals([gem, coil])
        return Item(
            item_type="ring",
            value=round(totals.value * 1.7),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Ring Maker"],
        )


class BlastingPowderChamberTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, metal_dust: Item, stone_dust: Item) -> Item:  # type: ignore
        self.validate_type(metal_dust, "metal dust")
        self.validate_type(stone_dust, "stone dust")

        totals = self.properties_totals([metal_dust, stone_dust])
        return Item(
            item_type="blasting powder",
            value=2,
            materials=1,
            sequence=totals.sequence + ["Blasting Powder Chamber"],
        )


class ExplosivesMakerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, blasting_powder: Item, casing_metal_or_ceramic: Item) -> Item:  # type: ignore
        self.validate_type(blasting_powder, "blasting powder")
        if (
            casing_metal_or_ceramic.item_type != "metal casing"
            and casing_metal_or_ceramic.item_type != "ceramic casing"
        ):
            raise Exception(
                f"Excepted metal or ceramic casing, got {casing_metal_or_ceramic.item_type} "
                + repr(casing_metal_or_ceramic)
            )

        totals = self.properties_totals([blasting_powder, casing_metal_or_ceramic])
        return Item(
            item_type="explosives",
            value=round(casing_metal_or_ceramic.value * blasting_powder.value),
            materials=totals.materials,
            tags=casing_metal_or_ceramic.tags,
            sequence=totals.sequence + ["Explosives Maker"],
        )


class CircuitMakerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, glass: Item, coil: Item) -> Item:  # type: ignore
        self.validate_type(glass, "glass")
        self.validate_type(coil, "coil")

        totals = self.properties_totals([glass, coil])
        return Item(
            item_type="circuit",
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Electronics"])),
            sequence=totals.sequence + ["Circuit Maker"],
        )


class ClayMixerTransformation:
    """dusts are stupid, use for dust related operations direct creation of predefined types items in Items.create_[something]
    might implement dust-related things after full 100% accurate implementation of Crusher, or who even cares about dusts outside of siefting"""

    pass


class MetalCasingTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, frame: Item, bolts: Item, plate: Item) -> Item:  # type: ignore
        self.validate_type(frame, "metal frame")
        self.validate_type(bolts, "bolts")
        self.validate_type(plate, "plate")

        totals = self.properties_totals([frame, bolts, plate])
        return Item(
            item_type="metal casing",
            value=round(totals.value * 1.3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Casing Machine"],
        )


class PrismaticGemCrucibleTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, gem1: Item, gem2: Item) -> Item:  # type: ignore
        self.validate_type(gem1, "gem")
        self.validate_type(gem2, "gem")
        self.validate_tag_absence(gem1, "Prismatic")
        self.validate_tag_absence(gem2, "Prismatic")

        totals = self.properties_totals([gem1, gem2])
        return Item(
            item_type="gem",
            value=round(totals.value * 1.15),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Prismatic"])),
            sequence=totals.sequence + ["Prismatic Gem Crucible"],
        )


class AlloyFurnaceTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, bar1: Item, bar2: Item) -> Item:  # type: ignore
        self.validate_type(bar1, "bar")
        self.validate_type(bar2, "bar")
        self.validate_tag_absence(bar1, "Alloyed")
        self.validate_tag_absence(bar2, "Alloyed")

        totals = self.properties_totals([bar1, bar2])
        return Item(
            item_type="bar",
            value=round(totals.value * 1.2),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Alloyed"])),
            sequence=totals.sequence + ["Alloy Furnace"],
        )


class MagneticMachineTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, coil: Item, metal_casing: Item) -> Item:  # type: ignore
        self.validate_type(coil, "coil")
        self.validate_type(metal_casing, "metal casing")

        totals = self.properties_totals([coil, metal_casing])
        return Item(
            item_type="electromagnet",
            value=round(totals.value * 1.5),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Electronics"])),
            sequence=totals.sequence + ["Magnetic Machine"],
        )


class OpticsMachineTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, lens: Item, pipe: Item) -> Item:  # type: ignore
        self.validate_type(lens, "lens")
        self.validate_type(pipe, "pipe")

        totals = self.properties_totals([lens, pipe])
        return Item(
            item_type="optics",
            value=round(totals.value * 1.25),
            materials=totals.materials,
            tags=list(set(totals.tags)),
            sequence=totals.sequence + ["Optics Machine"],
        )


class GilderTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, filigree: Item, jewellery: Item) -> Item:  # type: ignore
        self.validate_type(filigree, "filigree")
        self.validate_tag_absence(jewellery, "Gilded")
        if jewellery.item_type != "ring" and jewellery.item_type != "amulet":
            raise Exception(
                f"Excepted jewellery (rin or amulet), got {jewellery.item_type} "
                + repr(jewellery)
            )

        totals = self.properties_totals([filigree, jewellery])
        return Item(
            item_type=jewellery.item_type,
            value=round(totals.value * 1.2),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Gilded"])),
            sequence=totals.sequence + ["Gilder"],
        )


class EngineFactoryTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, mechanical_parts: Item, pipe: Item, metal_casing: Item) -> Item:  # type: ignore
        self.validate_type(mechanical_parts, "mechanical parts")
        self.validate_type(pipe, "pipe")
        self.validate_type(metal_casing, "metal casing")

        totals = self.properties_totals([mechanical_parts, pipe, metal_casing])
        return Item(
            item_type="engine",
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Engine Factory"],
        )


class SuperconductorConstructorTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, alloyed_bar: Item, ceramic_casing: Item) -> Item:  # type: ignore
        self.validate_type(alloyed_bar, "bar")
        self.validate_tag_present(alloyed_bar, "Alloyed")
        self.validate_type(ceramic_casing, "ceramic casing")

        totals = self.properties_totals([alloyed_bar, ceramic_casing])
        return Item(
            item_type="superconductor",
            value=round(totals.value * 3),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Superconductor Constructor"],
        )


class AmuletMakerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, ring: Item, frame: Item, prismatic_gem: Item) -> Item:  # type: ignore
        self.validate_type(ring, "ring")
        self.validate_type(frame, "metal frame")
        self.validate_type(prismatic_gem, "gem")
        self.validate_tag_present(prismatic_gem, "Prismatic")

        totals = self.properties_totals([ring, frame, prismatic_gem])
        return Item(
            item_type="amulet",
            value=round(totals.value * 2),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Amulter maker"],
        )


class TabletFactoryTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, metal_casing: Item, glass: Item, circuit: Item) -> Item:  # type: ignore
        self.validate_type(metal_casing, "metal casing")
        self.validate_type(glass, "glass")
        self.validate_type(circuit, "circuit")

        totals = self.properties_totals([metal_casing, glass, circuit])
        return Item(
            item_type="tablet",
            value=round(totals.value * 3),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Electronics"])),
            sequence=totals.sequence + ["Tablet Factory"],
        )


class BlastingPowderRefinerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    """Bruh, just skip this bullshit until later, if really need make Item(item_type="blasting powder", value=2, materials=2) or materials = 0 or whatever you want"""

    pass


class LaserTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform(self, optics: Item, gem: Item, circuit: Item) -> Item:  # type: ignore
        self.validate_type(optics, "optics")
        self.validate_type(gem, "gem")
        self.validate_type(circuit, "circuit")

        totals = self.properties_totals([optics, gem, circuit])
        return Item(
            item_type="laser",
            value=round(totals.value * 2.5),
            materials=totals.materials,
            tags=totals.tags,
            sequence=totals.sequence + ["Laser Maker"],
        )


class PowerCoreAssemblerTransformation(
    Transformation_Multiple, ValidationMixin, TransformationHelperMixin
):
    def transform( # type: ignore
        self, metal_casing: Item, superconductor: Item, electromagnet: Item
    ) -> Item:  # type: ignore
        self.validate_type(metal_casing, "metal casing")
        self.validate_type(superconductor, "superconductor")
        self.validate_type(electromagnet, "electromagnet")

        totals = self.properties_totals([metal_casing, superconductor, electromagnet])
        return Item(
            item_type="",
            value=round(totals.value * 2.5),
            materials=totals.materials,
            tags=list(set(totals.tags + ["Electronics"])),
            sequence=totals.sequence + ["Power Core Assembler"],
        )
