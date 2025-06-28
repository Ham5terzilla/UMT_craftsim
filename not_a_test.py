from crafting_system.constants import ItemTypes
from crafting_system.dataclasses.items import Item
from crafting_system.item_factory import ItemFactory
from crafting_system.transformations import transformations_multiple as tm
from crafting_system.transformations import transformations_single as ts

ore = "Unobtainium"
results: list[Item] = []
ore = ItemFactory.create_ore(ore)
results.append(ore)
ore_cleaned = ts.OreCleanerTransformation().transform(ore)
results.append(ore_cleaned)
ore_polished = ts.PolisherTransformation().transform(ore_cleaned)
results.append(ore_polished)
ore_infused = ts.PhilosophersStoneTransformation().transform(ore_polished)
results.append(ore_infused)
bar = ts.OreSmelterTransformation().transform(ore_infused)
results.append(bar)
alloy = tm.AlloyFurnaceTransformation().transform(bar, bar)
results.append(alloy)
alloy_tempered = ts.TemperingForgeTransformation().transform(alloy)
results.append(alloy_tempered)
gem = ts.BTGTransformation().transform(alloy_tempered)
results.append(gem)
gem_cut = ts.GemCutterTransformation().transform(gem)
results.append(gem_cut)
gem_prismatic = tm.PrismaticGemCrucibleTransformation().transform(gem_cut, gem_cut)
results.append(gem_prismatic)
super_gem = ts.QAMachineTransformation().transform(gem_prismatic)
results.append(super_gem)
super_alloy = ts.GTBTransformation().transform(super_gem)
results.append(super_alloy)

bar = super_alloy
gem = super_gem
coil = ts.CoilerTransformation().transform(bar)
results.append(coil)
bolts = ts.BoltMachineTransformation().transform(bar)
results.append(bolts)
plate = ts.PlateStamperTransformation().transform(bar)
results.append(plate)
pipe = ts.PipeMakerTransformation().transform(plate)
results.append(pipe)
mechanical_parts = ts.MechanicalPartsMakerTransformation().transform(plate)
results.append(mechanical_parts)
filigree = ts.FiligreeCutterTransformation().transform(plate)
results.append(filigree)

table2: list[Item] = []
frame = tm.FrameMakerTransformation().transform(bar, bolts)
table2.append(frame)
ring = tm.RingMakerTransformation().transform(gem, coil)
table2.append(ring)
stupid_dust_x2 = Item(ItemTypes.BLASTING_POWDER, value=2, materials=0, sequence=["STUPID_DUST_x2"])
stupid_dust_x3 = Item(ItemTypes.BLASTING_POWDER, value=3, materials=0, sequence=["STUPID_DUST_x2"])
metal_casing = tm.CasingMachineTransformation().transform(frame, bolts, plate)
table2.append(metal_casing)
explosives_2x = tm.ExplosivesMakerTransformation().transform(stupid_dust_x2, metal_casing)
table2.append(explosives_2x)
explosives_3x = tm.ExplosivesMakerTransformation().transform(stupid_dust_x3, metal_casing)
table2.append(explosives_3x)
stupid_glass = Item(
    item_type=ItemTypes.GLASS, value=40, materials=0, sequence=["STUPID_GLASS_POLISHED"]
)
circuit = tm.CircuitMakerTransformation().transform(stupid_glass, coil)
circuit = ts.ElectronicTunerTransformation().transform(circuit)
table2.append(circuit)
stupid_ceramic_casing = Item(
    item_type=ItemTypes.CERAMIC_CASING,
    value=160,
    materials=0,
    sequence=["STUPID_CERAMICS_ALSO_POLISHED"],
)
stupid_lens = Item(
    item_type=ItemTypes.LENS,
    value=60,
    materials=0,
    sequence=["ANOTHER_STUPID_ITEM_POLISHED"],
)
electromagnet = tm.MagneticMachineTransformation().transform(coil, metal_casing)
electromagnet = ts.ElectronicTunerTransformation().transform(electromagnet)
table2.append(electromagnet)
optics = tm.OpticsMachineTransformation().transform(stupid_lens, pipe)
table2.append(optics)
engine = tm.EngineFactoryTransformation().transform(mechanical_parts, pipe, metal_casing)
table2.append(optics)
superconductor = tm.SuperconductorConstructorTransformation().transform(bar, stupid_ceramic_casing)
table2.append(superconductor)
amulet = tm.AmuletMakerTransformation().transform(ring, frame, gem)
table2.append(amulet)
amulet_gilded = tm.GilderTransformation().transform(filigree, amulet)
table2.append(amulet_gilded)
ring_gilded = tm.GilderTransformation().transform(filigree, ring)
table2.append(ring_gilded)
tablet = tm.TabletFactoryTransformation().transform(metal_casing, stupid_glass, circuit)
table2.append(tablet)
laser = tm.LaserMakerTransformation().transform(optics, gem, circuit)
table2.append(laser)
power_core = tm.PowerCoreAssemblerTransformation().transform(
    metal_casing, superconductor, electromagnet
)
table2.append(power_core)


for result in results:
    print(result)
print()
for _ in table2:
    print(_.table_full())
