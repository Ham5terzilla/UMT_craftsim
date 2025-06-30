"""
Central registry for machine-to-transformation mappings.
"""

from crafting_system.constants import Machines
from crafting_system.transformations import transformations_multiple, transformations_single
from crafting_system.transformations.transformations_multiple import Transformation_Multiple
from crafting_system.transformations.transformations_single import Transformation_Single


class TransformationRegistry:
    """Central catalog mapping crafting machines to their transformation logic.
    
    Attributes:
        registry (dict[Machines, Transformation_Single | Transformation_Multiple | None]):
            Complete mapping of all machines to their corresponding transformation classes.
            None indicates unimplemented transformations.
    
    ## Methods
        get_transformation: Retrieves transformation class for a given machine
    
    Example:
        frame_maker = TransformationRegistry.get_transformation("Frame Maker")
        frame = frame_maker().transform(bar, bolts)
    """

    registry = {
        Machines.ORE_CLEANER: transformations_single.OreCleanerTransformation,
        Machines.POLISHER: transformations_single.PolisherTransformation,
        Machines.ELECTRONIC_TUNER: transformations_single.PolisherTransformation,
        Machines.GEM_CUTTER: transformations_single.GemCutterTransformation,
        Machines.TEMPERING_FORGE: transformations_single.TemperingForgeTransformation,
        Machines.QUALITY_ASSURANCE_MACHINE: transformations_single.QAMachineTransformation,
        Machines.PHILOSOPHERS_STONE: transformations_single.PhilosophersStoneTransformation,
        Machines.ORE_UPGRADER: transformations_single.OreUpgraderTransformation,
        Machines.TOPAZ_PROSPECTOR: None,
        Machines.EMERALD_PROSPECTOR: None,
        Machines.SAPPHIRE_PROSPECTOR: None,
        Machines.RUBY_PROSPECTOR: None,
        Machines.DIAMOND_PROSPECTOR: None,
        Machines.ORE_SMELTER: transformations_single.OreSmelterTransformation,
        Machines.CRUSHER: transformations_single.CrusherTransformation,
        Machines.COILER: transformations_single.CoilerTransformation,
        Machines.BRICK_MOLD: None,
        Machines.BOLT_MACHINE: transformations_single.BoltMachineTransformation,
        Machines.PLATE_STAMPER: transformations_single.PlateStamperTransformation,
        Machines.SIFTER: None,
        Machines.PIPE_MAKER: transformations_single.PipeMakerTransformation,
        Machines.KILN: None,
        Machines.MECHANICAL_PARTS_MAKER: transformations_single.MechanicalPartsMakerTransformation,
        Machines.BLAST_FURNACE: transformations_single.BlastFurnaceTransformation,
        Machines.CERAMIC_FURNACE: transformations_single.CeramicFurnaceTransformation,
        Machines.FILIGREE_CUTTER: transformations_single.FiligreeCutterTransformation,
        Machines.LENS_CUTTER: transformations_single.LensCutterTransformation,
        Machines.DUPLICATOR: transformations_single.DuplicatorTransformation,
        Machines.NANO_SIFTER: None,
        Machines.GEM_TO_BAR_TRANSMUTER: transformations_single.GTBTransformation,
        Machines.BAR_TO_GEM_TRANSMUTER: transformations_single.BTGTransformation,
        Machines.CEMENT_MIXER: None,
        Machines.FRAME_MAKER: transformations_multiple.FrameMakerTransformation,
        Machines.RING_MAKER: transformations_multiple.RingMakerTransformation,
        Machines.BLASTING_POWDER_CHAMBER: transformations_multiple.BlastingPowderChamberTransformation,
        Machines.EXPLOSIVES_MAKER: transformations_multiple.ExplosivesMakerTransformation,
        Machines.CIRCUIT_MAKER: transformations_multiple.CircuitMakerTransformation,
        Machines.CLAY_MIXER: transformations_multiple.ClayMixerTransformation,
        Machines.CASING_MACHINE: transformations_multiple.CasingMachineTransformation,
        Machines.PRISMATIC_GEM_CRUCIBLE: transformations_multiple.PrismaticGemCrucibleTransformation,
        Machines.ALLOY_FURNACE: transformations_multiple.AlloyFurnaceTransformation,
        Machines.MAGNETIC_MACHINE: transformations_multiple.MagneticMachineTransformation,
        Machines.OPTICS_MACHINE: transformations_multiple.OpticsMachineTransformation,
        Machines.GILDER: transformations_multiple.GilderTransformation,
        Machines.ENGINE_FACTORY: transformations_multiple.EngineFactoryTransformation,
        Machines.SUPERCONDUCTOR_CONSTRUCTOR: transformations_multiple.SuperconductorConstructorTransformation,
        Machines.AMULET_MAKER: transformations_multiple.AmuletMakerTransformation,
        Machines.TABLET_FACTORY: transformations_multiple.TabletFactoryTransformation,
        Machines.BLASTING_POWDER_REFINER: transformations_multiple.BlastingPowderRefinerTransformation,
        Machines.LASER_MAKER: transformations_multiple.LaserMakerTransformation,
        Machines.POWER_CORE_ASSEMBLER: transformations_multiple.PowerCoreAssemblerTransformation,
    }

    @classmethod
    def get_transformation(
        cls, machine_name: str | Machines
    ) -> Transformation_Multiple | Transformation_Single:
        """Retrieves transformation class for a crafting machine.\n
        Provides machine name resolution from both string identifiers and enum members.

        Args:
            machine_name (str | Machines): Machine identifier (case-insensitive string or Machines enum)

        Raises:
            KeyError: For invalid/unregistered machine names
            NotImplementedError: if transformation for machine is found, but not implemented

        Returns:
            Transformation class (callable) for the specified machine
        
        Example:
            Using enum\n
            smelter = TransformationRegistry.get_transformation(Machines.ORE_SMELTER)
            
            Using string\n
            cleaner = TransformationRegistry.get_transformation("Ore Cleaner")
        """

        if isinstance(machine_name, str):
            if machine_name.upper() in Machines.__members__.keys():
                machine_name = Machines[machine_name.upper()]
            else:
                raise KeyError(f"Machine with name {machine_name} not found in Machines")
        if machine_name not in cls.registry:
            raise KeyError(f"Transformation for {machine_name} not found")
        elif not cls.registry[machine_name]:
            raise NotImplementedError(f"Transformation class for {machine_name} not implemented")
        else:
            return cls.registry[machine_name]
