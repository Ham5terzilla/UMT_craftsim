"""
module with registry class for transformation. It works, but I'm not sure what to do with that, currently seems too complicated.\n
In case if someone would use it, need to finish TransformationRegistry.registry dict
"""

from crafting_system.constants import Machines
from crafting_system.transformations import transformations_multiple, transformations_single
from crafting_system.transformations.transformations_multiple import Transformation_Multiple
from crafting_system.transformations.transformations_single import Transformation_Single


class TransformationRegistry:
    """
    unfinished, purpose of this class is self.registry dict with keys as objects from Machines and tranformations from corresponding modules\n
    contains:
        self.registry: dict[Machines, transformation_single | transformation_multiple | None]
        get_transformation method, which input str or constant from Machines and returns corresponding transformation class
    """

    registry = {
        Machines.BAR_TO_GEM_TRANSMUTER: transformations_single.BTGTransformation,
        Machines.BLAST_FURNACE: transformations_single.BlastFurnaceTransformation,
        Machines.BOLT_MACHINE: transformations_single.BoltMachineTransformation,
        Machines.CERAMIC_FURNACE: transformations_single.CeramicFurnaceTransformation,
        Machines.BRICK_MOLD: None,
        Machines.COILER: transformations_single.CoilerTransformation,
        Machines.CRUSHER: transformations_single.CrusherTransformation,
        Machines.DIAMOND_PROSPECTOR: None,
        Machines.ALLOY_FURNACE: transformations_multiple.AlloyFurnaceTransformation,
        Machines.AMULET_MAKER: transformations_multiple.AmuletMakerTransformation,
        Machines.BLASTING_POWDER_CHAMBER: transformations_multiple.BlastingPowderChamberTransformation,
        Machines.BLASTING_POWDER_REFINER: transformations_multiple.BlastingPowderRefinerTransformation,
        Machines.CASING_MACHINE: transformations_multiple.CasingMachineTransformation,
        Machines.CEMENT_MIXER: None,
        Machines.CIRCUIT_MAKER: transformations_multiple.CircuitMakerTransformation,
        Machines.CLAY_MIXER: transformations_multiple.ClayMixerTransformation,
        Machines.DUPLICATOR: transformations_single.DuplicatorTransformation,
    }

    @classmethod
    def get_transformation(
        cls, machine_name: str | Machines
    ) -> Transformation_Multiple | Transformation_Single:
        """Get corresponding transformation class from name of machine, based on dict \n
        with keys equals to keys in constants.Machines and values equals classes in transformations_single.py and *_multiple.py

        Args:
            machine_name (str | Machines): can be directly part of Machines class or key of Machines, as used as key in TransformationRegistry.registry dict

        Raises:
            KeyError: if machine with name machine_name not found in constants.Machines
            KeyError: if transformation for machine with machine_name not found
            NotImplementedError: if transformation for machine is found, but not implemented

        Returns:
            Transformation class corresponding to machine if found successful
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
