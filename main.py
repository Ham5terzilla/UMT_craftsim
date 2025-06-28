from crafting_system.dataclasses.items import Item
from crafting_system.item_builder import ItemBuilder
from crafting_system.item_factory import ItemFactory
from crafting_system.transformations import transformations_multiple as tm
from crafting_system.transformations import transformations_single as ts

# Usage of project. This code doesn't interacting with code base, can be modified anyhow, it's literally just usage.
# I decided to not cut this for having example of systems, so, everyone downloaded this garbage from github can start from something before going deeper.
tin = ItemFactory.create_ore("Tin")
tin_bar = (
    ItemBuilder(tin)
    .add_transformation_single(ts.OreCleanerTransformation())
    .add_transformation_single(ts.PolisherTransformation())
    .add_transformation_single(ts.OreSmelterTransformation())
    .execute()
)
tin_alloy_untempered = tm.AlloyFurnaceTransformation().transform(tin_bar, tin_bar)
tin_alloy = ts.TemperingForgeTransformation().transform(tin_alloy_untempered)
tin_bolts = ts.BoltMachineTransformation().transform(tin_alloy)
tin_coil = ts.CoilerTransformation().transform(tin_alloy)
tin_plate = ts.PlateStamperTransformation().transform(tin_alloy)
tin_frame = tm.FrameMakerTransformation().transform(tin_alloy, tin_bolts)
tin_casing = tm.CasingMachineTransformation().transform(tin_frame, tin_bolts, tin_plate)
tin_electromagnet = tm.MagneticMachineTransformation().transform(tin_coil, tin_casing)
tin_electromagnet_tuned = ts.ElectronicTunerTransformation().transform(tin_electromagnet)
print(tin)
print(tin_bar)
print(tin_alloy)
print(tin_bolts)
print(tin_coil)
print(tin_plate)
print(tin_frame)
print(tin_casing)
print(tin_electromagnet)
print(tin_electromagnet_tuned)
print()
stupid_glass = Item("glass", 30)
tin_circuit_untuned = tm.CircuitMakerTransformation().transform(stupid_glass, tin_coil)
tin_circuit = ts.ElectronicTunerTransformation().transform(tin_circuit_untuned)
tin_tablet = tm.TabletFactoryTransformation().transform(tin_casing, stupid_glass, tin_circuit)
print(repr(tin_tablet))

painite = ItemFactory.create_gem("Painite")
painite_stage1_processed = (
    ItemBuilder(painite)
    .add_transformation_single(ts.PolisherTransformation())
    .add_transformation_single(ts.GemCutterTransformation())
    .execute()
)
painite_prismatic = tm.PrismaticGemCrucibleTransformation().transform(
    painite_stage1_processed, painite_stage1_processed
)
painite_bar = ts.GTBTransformation().transform(painite_prismatic)
painite_alloy_untempered = tm.AlloyFurnaceTransformation().transform(painite_bar, painite_bar)
painite_alloy = ts.TemperingForgeTransformation().transform(painite_alloy_untempered)
print(painite_stage1_processed.table_full())
print(painite_prismatic.table_full())
print(painite_bar.table_full())
print(painite_alloy_untempered.table_full())
print(painite_alloy.table_full())
