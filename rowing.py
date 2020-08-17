from time import sleep
from py4j.java_gateway import JavaGateway

gateway = JavaGateway(auto_convert=True)
mc = gateway.entry_point

for i in range(1, 300):
    mc.put_and_get("rowing", {"x": "100", "y": "119", "z": "1"})
    sleep(0.2)