from time import sleep
from py4j.java_gateway import JavaGateway

gateway = JavaGateway(auto_convert=True)

for i in range(3000):
    gateway.entry_point.put("nearby_mods", {"sid" : "1"})
    sleep(2)
    result = gateway.entry_point.get("1")
    if result and int(result["count"]) >= 1:
        gateway.entry_point.put("attack", {"x" : "4712", "y" : "40", "z" : "-3372"})
        sleep(1)
        gateway.entry_point.put("attack", {"x" : "4712", "y" : "40", "z" : "-3372"})
    sleep(1)