from time import sleep
from py4j.java_gateway import JavaGateway

gateway = JavaGateway(auto_convert=True)
mc = gateway.entry_point

default = {"default" : ""}

for x in range(30173, 30174):
    for y in range(63, 67):
        mc.put_and_get("use_block", {"x": str(x), "y": str(y), "z": "1141"})
        sleep(1)
        mc.put_and_get("chest_cache", {"group" : "ustc", "x": str(x), "y": str(y), "z": "1141"})
        mc.put_and_get("close_container", default)
        sleep(1)
        
        
mc.put_and_get("move", {"x": "238", "y": "6", "z": "10"})

mc.put_and_get(")