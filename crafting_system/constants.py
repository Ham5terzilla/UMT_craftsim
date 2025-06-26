"""
Module full of constants
"""

from enum import StrEnum, auto


class ItemTypes(StrEnum):
    UNKNOWN = auto()
    ORE = auto()
    GEM = auto()

    STONE = auto()
    DUST = auto()
    BLASTING_POWDER = auto()
    BRICK = auto()
    CLAY_BLOCK = auto()
    GLASS = auto()
    LENS = auto()
    CEMENT = auto()
    CONCRETE_BRICK = auto()
    CERAMIC_CASING = auto()

    BAR = auto()
    COIL = auto()
    BOLTS = auto()
    PLATE = auto()
    PIPE = auto()
    MECHANICAL_PARTS = auto()
    FILIGREE = auto()

    RING = auto()
    FRAME = auto()
    EXPLOSIVES = auto()
    CIRCUIT = auto()
    METAL_CASING = auto()
    ELECTROMAGNET = auto()
    OPTICS = auto()
    ENGINE = auto()
    SUPERCONDUCTOR = auto()
    AMULET = auto()
    TABLET = auto()
    LASER = auto()
    POWER_CORE = auto()


class DustTypes(StrEnum):
    UNKNOWN = auto()
    METALL = auto()
    STONE = auto()
    GEM = auto()


class Tags(StrEnum):
    # not all tags from game atm
    UNKNOWN = "UNKNOWN"
    ALLOYED = "Alloyed"  # Persists after crusher (tested)
    CLEANED = "Cleaned"
    PLATE = "Plate"
    TEMPERED = "Tempered"
    SIFTED = "Sifted"  # Persists after crusher (tested)
    PRISMATIC = "Prismatic"  # Persists after crusher?
    QUALITY_ASSURED = "Quality Assured"
    UPGRADED = "Upgraded"
    METAL_FRAME = "Metal Frame"
    SMELTED = "Smelted"
    CUT = "Cut"
    DRAWN = "Drawn"
    POLISHED = "Polished"
    CERAMIC = "Ceramic"
    BOLTS = "Bolts"
    DUPLICATED = "Duplicated"  # Persists after crusher?
    SUPERCONDUCTOR = "Superconductor"
    GOLD_INFUSED = "Gold Infused"
    METAL_CASING = "Metal Casing"
    MECHANICAL_PARTS = "MechanicalParts"
    PIPE = "Pipe"
    TUNED = "Tuned"
    FILIGREE = "Filigree"
    GILDED = "Gilded"


class Machines(StrEnum):
    UNKNOWN = "UNKNOWN"
    ORE_CLEANER = "Ore Cleaner"
    POLISHER = "Polisher"
    ELECTRONIC_TUNER = "Electronic Tuner"
    GEM_CUTTER = "Gem Cutter"
    TEMPERING_FORGE = "Tempering Forge"
    QUALITY_ASSURANCE_MACHINE = "Quality Assurance Machine"
    PHILOSOPHERS_STONE = "Philosophers Stone"
    ORE_UPGRADER = "Ore Upgrader"

    TOPAZ_PROSPECTOR = "Topaz Prospector"
    EMERALD_PROSPECTOR = "Emerald Prospector"
    SAPPHIRE_PROSPECTOR = "Sapphire Prospector"
    RUBY_PROSPECTOR = "Ruby Prospector"
    DIAMOND_PROSPECTOR = "Diamond Prospector"

    ORE_SMELTER = "Ore Smelter"
    CRUSHER = "Crusher"
    COILER = "Coiler"
    BRICK_MOLD = "Brick Mold"
    BOLT_MACHINE = "Bolt Machine"
    PLATE_STAMPER = "Plate Stamper"
    SIFTER = "Sifter"
    PIPE_MAKER = "Pipe Maker"
    KILN = "Kiln"
    MECHANICAL_PARTS_MAKER = "Mechanical Parts Maker"
    BLAST_FURNACE = "Blast Furnace"
    CERAMIC_FURNACE = "Ceramic Furnace"
    FILIGREE_CUTTER = "Filigree Cutter"
    LENS_CUTTER = "Lens Cutter"
    DUPLICATOR = "Duplicator"
    NANO_SIFTER = "Nano Sifter"
    GEM_TO_BAR_TRANSMUTER = "Gem To Bar Transmuter"
    BAR_TO_GEM_TRANSMUTER = "Bar To Gem Transmuter"

    CEMENT_MIXER = "Cement Mixer"
    FRAME_MAKER = "Frame Maker"
    RING_MAKER = "Ring Maker"
    BLASTING_POWDER_CHAMBER = "Blasting Powder Chamber"
    EXPLOSIVES_MAKER = "Explosives Maker"
    CIRCUIT_MAKER = "Circuit Maker"
    CLAY_MIXER = "Clay Mixer"
    CASING_MACHINE = "Casing Machine"
    PRISMATIC_GEM_CRUCIBLE = "Prismatic Gem Crucible"
    ALLOY_FURNACE = "Alloy Furnace"
    MAGNETIC_MACHINE = "Magnetic Machine"
    OPTICS_MACHINE = "Optics Machine"
    GILDER = "Gilder"
    ENGINE_FACTORY = "Engine Factory"
    SUPERCONDUCTOR_CONSTRUCTOR = "Superconductor Constructor"
    AMULET_MAKER = "Amulet Maker"
    TABLET_FACTORY = "Tablet Factory"
    BLASTING_POWDER_REFINER = "Blasting Powder Refiner"
    LASER_MAKER = "Laser Maker"
    POWER_CORE_ASSEMBLER = "Power Core Assembler"
