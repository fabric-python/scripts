from time import sleep
from py4j.java_gateway import JavaGateway

gateway = JavaGateway(auto_convert=True)
mc = gateway.entry_point

res = mc.put_and_get("switch_items", {"name" : "minecraft:netherite_sword"})
if res and res["res"] == "failure":
    mc.put_and_get("switch_items", {"name": "minecraft:diamond_sword"})

default = {"default" : ""}

for i in range(3000):
    nearby_wither_skeletons = mc.put_and_get("nearby_mods", {"type" : "wither_skeleton"})

    if nearby_wither_skeletons and int(nearby_wither_skeletons["count"]) >= 1:
        mc.put_and_get("attack", {"type" : "wither_skeleton", "x": "4712", "y": "40", "z": "-3372"})
        sleep(1)

    nearby_magma_cubes = mc.put_and_get("nearby_mods", {"type": "magma_cube"})

    if nearby_magma_cubes and int(nearby_magma_cubes["count"] >= 1):
        mc.put_and_get("attack", {"type": "nearby_magma_cubes", "x": "4712", "y": "40", "z": "-3372"})
        sleep(1)

    hungry = mc.put_and_get("hungry", default)
    if hungry and int(hungry["res"]) <= 12:
        mc.put_and_get("switch_items", {"name": "minecraft:cooked_porkchop"})
        mc.put_and_get("use", default)
        sleep(2)
        res = mc.put_and_get("switch_items", {"name": "minecraft:netherite_sword"})
        if res and res["res"] == "failure":
            mc.put_and_get("switch_items", {"name": "minecraft:diamond_sword"})
        sleep(1)