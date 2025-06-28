"""
Factory for creating game items with predefined names and recipes
"""

from crafting_system.constants import Gems, ItemTypes, Machines, Ores
from crafting_system.dataclasses.items import Item
from crafting_system.service.exceptions import ItemProcessingError
from crafting_system.service.mixins import TransformationHelperMixin
from crafting_system.transformations import transformations_multiple as tmultiple
from crafting_system.transformations import transformations_single as tsingle


class ItemFactory:
    """
    ItemFactory class, allows easier creation of various items from given alloy and gem.\n
    Also provides staticmethods, such as create_ore(str)->Item, create_gem(str)->Item, for easier workaround
    """

    def __init__(self, alloy: Item | None = None, gem: Item | None = None):
        """ItemFactory init, ItemFactory uses internal alloy and gem in recipes, for more flexibility use ItemBuilder and transformation classes directly.

        Args:
            alloy (Item | None): alloy which would be used in recipes from ItemFactory, optional, until alloy involved in recipe
            gem (Item | None): gem which would be used in recipes from ItemFactory, optional, until gem involbed in recipe
        """
        self.alloy: Item | None = alloy if alloy else None
        self.gem: Item | None = gem if gem else None

    @staticmethod
    def create_ore(ore_name: str | Ores) -> Item:
        """Creates Item object with type ore and value based on name

        Args:
            ore_name (str): constant from constants.OreNames class

        Returns:
            Item: Item obj, Item(item_type=ItemTypes.ORE, value=value from OreNames by name)
        """
        value = Ores[ore_name.upper()].value if isinstance(ore_name, str) else ore_name.value
        return Item(item_type=ItemTypes.ORE, value=value)

    @staticmethod
    def create_gem(gem_name: str | Gems) -> Item:
        """Creates Item object with type gem and value based on name

        Args:
            gem_name (str): constant from constants.GemNames class

        Returns:
            Item: Item obj, Item(item_type=ItemTypes.GEM, value=value from GemNames by name)
        """
        value = Gems[gem_name.upper()].value if isinstance(gem_name, str) else gem_name.value
        return Item(item_type=ItemTypes.GEM, value=value)

    @staticmethod
    def process_mats_simple(ore_or_gem: Item, machines: list[Machines]) -> Item:
        """Process material using machines from list in certain sequence, outputs final item without any verboose.\n
        Sequence can't be changed, for more flexibility and control use transformation classes directly.\n
        Sequence:\n
        Ore Upgrader -> Ore Cleaner -> Polisher -> Philosophers Stone -> Ore Smelter|Blast Furnace ->\n
        BTG -> Prismatic Gem Crucible -> Gem Cutter -> GTB -> Alloy Furnace -> Tempering Forge

        Args:
            ore_or_gem (Item): ore or gem before processing, can be created by ItemFactory.create_ore or *_gem
            machines (list[Machines]): list of allowed machines for item processing

        Returns:
            Item: item after processing sequence
        """
        TransformationHelperMixin.validate_multiple_items_types(
            [ore_or_gem], [ItemTypes.ORE, ItemTypes.GEM]
        )

        if Machines.ORE_UPGRADER in machines and ore_or_gem.item_type == ItemTypes.ORE:
            ore_or_gem = tsingle.OreUpgraderTransformation().transform(ore_or_gem)
        if Machines.ORE_CLEANER in machines and ore_or_gem.item_type == ItemTypes.ORE:
            ore_or_gem = tsingle.OreCleanerTransformation().transform(ore_or_gem)
        if Machines.POLISHER in machines:
            ore_or_gem = tsingle.PolisherTransformation().transform(ore_or_gem)
        if Machines.PHILOSOPHERS_STONE in machines and ore_or_gem.item_type == ItemTypes.ORE:
            ore_or_gem = tsingle.PhilosophersStoneTransformation().transform(ore_or_gem)
        if Machines.ORE_SMELTER in machines and ore_or_gem.item_type == ItemTypes.ORE:
            ore_or_gem = tsingle.OreSmelterTransformation().transform(ore_or_gem)
        elif Machines.BLAST_FURNACE in machines and ore_or_gem.item_type == ItemTypes.ORE:
            ore_or_gem = tsingle.BlastFurnaceTransformation().transform(ore_or_gem)
        if Machines.BAR_TO_GEM_TRANSMUTER in machines and ore_or_gem.item_type == ItemTypes.BAR:
            ore_or_gem = tsingle.BTGTransformation().transform(ore_or_gem)
        if Machines.PRISMATIC_GEM_CRUCIBLE in machines and ore_or_gem.item_type == ItemTypes.GEM:
            ore_or_gem = tmultiple.PrismaticGemCrucibleTransformation().transform(
                ore_or_gem, ore_or_gem
            )
        if Machines.GEM_CUTTER in machines and ore_or_gem.item_type == ItemTypes.GEM:
            ore_or_gem = tsingle.GemCutterTransformation().transform(ore_or_gem)
        if Machines.GEM_TO_BAR_TRANSMUTER in machines and ore_or_gem.item_type == ItemTypes.GEM:
            ore_or_gem = tsingle.GTBTransformation().transform(ore_or_gem)
        if Machines.ALLOY_FURNACE in machines and ore_or_gem.item_type == ItemTypes.BAR:
            ore_or_gem = tmultiple.AlloyFurnaceTransformation().transform(ore_or_gem, ore_or_gem)
        if Machines.TEMPERING_FORGE in machines and ore_or_gem.item_type == ItemTypes.BAR:
            ore_or_gem = tsingle.TemperingForgeTransformation().transform(ore_or_gem)
        return ore_or_gem

    @staticmethod
    def process_mats_complex(
        machines: list[Machines],
        item1: Item,
        item2: Item,
        item3: Item | None = None,
        item4: Item | None = None,
    ) -> Item:
        """
        Process material using machines from list in certain sequence, outputs final item without any verboose.\n
        Sequence can't be changed, for more flexibility and control use transformation classes directly.\n
        Sequence:\n
        Ore Upgrader -> Ore Cleaner -> Polisher -> Philosophers Stone -> Ore Smelter|Blast Furnace ->\n
        BTG -> Prismatic Gem Crucible -> Gem Cutter -> GTB -> Alloy Furnace -> Tempering Forge

        Args:
            machines (list[Machines]): list of allowed machines for item processing
            item1 (Item): ore or gem before processing
            item2 (Item): ore or gem before processing
            item3 (Item | None, optional): ore or gem before processing. Defaults to None.
            item4 (Item | None, optional): ore or gem before processing. Defaults to None.

        Raises:
            ItemProcessingError: if 4 items used but alloy furnace and gem crucible not present
            ItemProcessingError: if not present at least 1 of alloy furnace or crucible
            ItemProcessingError: if gem crucible was present but we got 1 or 3 gems after processing before crucible
            ItemProcessingError: if after all processes before Alloy Furnace more than 2 items present
            ItemProcessingError: if alloy furnace provided with items with different type

        Returns:
            Item: item after processing sequence
        """
        items: list[Item] = [item for item in [item1, item2, item3, item4] if item]
        TransformationHelperMixin.validate_multiple_items_types(
            items, [ItemTypes.ORE, ItemTypes.GEM]
        )
        if len(items) == 4 and (
            Machines.ALLOY_FURNACE not in machines
            or Machines.PRISMATIC_GEM_CRUCIBLE not in machines
        ):
            raise ItemProcessingError(
                f"For 4 items must be both {Machines.ALLOY_FURNACE} and {Machines.PRISMATIC_GEM_CRUCIBLE}"
            )
        if (
            Machines.ALLOY_FURNACE not in machines
            and Machines.PRISMATIC_GEM_CRUCIBLE not in machines
        ):
            raise ItemProcessingError(
                f"Must be present {Machines.ALLOY_FURNACE} or {Machines.PRISMATIC_GEM_CRUCIBLE}"
            )
        step1: list[Item] = []
        for item in items:
            if Machines.ORE_UPGRADER in machines and item.item_type == ItemTypes.ORE:
                item = tsingle.OreUpgraderTransformation().transform(item)
            if Machines.ORE_CLEANER in machines and item.item_type == ItemTypes.ORE:
                item = tsingle.OreCleanerTransformation().transform(item)
            if Machines.POLISHER in machines:
                item = tsingle.PolisherTransformation().transform(item)
            if Machines.PHILOSOPHERS_STONE in machines and item.item_type == ItemTypes.ORE:
                item = tsingle.PhilosophersStoneTransformation().transform(item)
            if Machines.ORE_SMELTER in machines and item.item_type == ItemTypes.ORE:
                item = tsingle.OreSmelterTransformation().transform(item)
            elif Machines.BLAST_FURNACE in machines and item.item_type == ItemTypes.ORE:
                item = tsingle.BlastFurnaceTransformation().transform(item)
            if Machines.BAR_TO_GEM_TRANSMUTER in machines and item.item_type == ItemTypes.BAR:
                item = tsingle.BTGTransformation().transform(item)
            step1.append(item)
        gems = [gem for gem in step1 if gem.item_type == ItemTypes.GEM]
        step2 = [item for item in step1 if item not in gems]
        if Machines.PRISMATIC_GEM_CRUCIBLE in machines:
            if len(gems) % 2 != 0:
                raise ItemProcessingError(
                    f"Excepted 2 or 4 gems to be processed by {Machines.PRISMATIC_GEM_CRUCIBLE} got {len(gems)}"
                )
            combined = [tmultiple.PrismaticGemCrucibleTransformation().transform(gems[0], gems[1])]
            if len(gems) == 4:
                combined.append(
                    tmultiple.PrismaticGemCrucibleTransformation().transform(gems[2], gems[3])
                )
            gems = combined
        step2 = step2 + gems
        step3: list[Item] = []
        for item in step2:
            if Machines.GEM_CUTTER in machines and item.item_type == ItemTypes.GEM:
                item = tsingle.GemCutterTransformation().transform(item)
            if Machines.GEM_TO_BAR_TRANSMUTER in machines and item.item_type == ItemTypes.GEM:
                item = tsingle.GTBTransformation().transform(item)
            step3.append(item)
        if len(step3) > 2:
            raise ItemProcessingError(
                f"Something went wrong, excepted 1 or 2 items, got {len(step3)} items"
            )
        final_item: Item = step3[0]
        if len(step3) == 2:
            if Machines.ALLOY_FURNACE in machines:
                if step3[0].item_type == ItemTypes.BAR == step3[1].item_type:
                    final_item = tmultiple.AlloyFurnaceTransformation().transform(
                        step3[0], step3[1]
                    )
                else:
                    raise ItemProcessingError(
                        f"{Machines.ALLOY_FURNACE} involved, but last 2 items types is {step3[0].item_type} and {step3[1].item_type}"
                    )
        if Machines.TEMPERING_FORGE in machines and final_item.item_type == ItemTypes.BAR:
            final_item = tsingle.TemperingForgeTransformation().transform(final_item)
        return final_item
