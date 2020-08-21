from time import sleep
from py4j.java_gateway import JavaGateway

gateway = JavaGateway(auto_convert=True)
mc = gateway.entry_point

default = {"default" : ""}

mc.put_and_get("send_chat_message", {"message": "/autotorch"});
mc.put_and_get("send_chat_message", {"message": "/automine"});

y_height = 47

flag = 0
loop = 0
while 1: 
    loop = loop + 1
    if loop % 10 == 1:
        if flag == 0:
            # check if the inventory is full
            nospace_res = mc.put_and_get("nospace", default)
            if nospace_res["res"] == "1":
                flag = 1
                print("DEBUG: no space")

        if flag == 0:
            # switch torchs to the off hand
            torch_res = mc.put_and_get("switch_items", {"name": "minecraft:torch", "hand": "off"})
            if torch_res["res"] != "success" and torch_res["res"] != "already in the off hand":
                flag = 1
                print("DEBUG: off hand no torch")

        if flag == 0:
            # switch the pickaxe to the main hand
            pickaxe_res = mc.put_and_get("switch_items", {"name": "minecraft:netherite_pickaxe"})
            if pickaxe_res["res"] != "success" and pickaxe_res["res"] != "already in the main hand":
                flag = 1
                print("DEBUG: main hand no pickaxe")
                
        if flag == 0:
            hungry = mc.put_and_get("hungry", default)
            if hungry and int(hungry["res"]) <= 12:
                mc.put_and_get("switch_items", {"name": "minecraft:cooked_cod"})
                mc.put_and_get("use", default)
                sleep(0.5)
                res = mc.put_and_get("switch_items", {"name": "minecraft:netherite_pickaxe"})
                sleep(0.5)
    
    if flag == 0:
        # find a block that can be mined
        nearby_block_res = mc.put_and_get("find_safe_mine_block", default)
        if not nearby_block_res["x"]:
            flag = 1
            print("DEBUG: no nearby safe mine block")
    
    if flag == 0:
        # move to the block with 3 attempts
        flag_moved = 0
        for i in range(3):
            move_result = mc.put_and_get("move", {"x": nearby_block_res["x_standing"], "y": nearby_block_res["y_standing"], "z": nearby_block_res["z_standing"], "nojump": "1"})
            if move_result["res"] and float(move_result["res"]) < 6:
                flag_moved = 1
                break;
        if flag_moved == 0:
            flag = 1
            print("DEBUG: cannot move")
    
    if flag == 0:
        # start breaking
        start_breaking_res = mc.put_and_get("start_mine", nearby_block_res)
        if not start_breaking_res["res"]:
            flag = 1
            print("DEBUG: cannot staert breaking")
    
    if flag == 0:
        # finish breaking
        if float(start_breaking_res["res"]) > 0:
            time = float(start_breaking_res["res"])
            sleep(1.0 / time)
            finish_breaking_res = mc.put_and_get("finish_mine", nearby_block_res)
            if (not finish_breaking_res["res"]) or finish_breaking_res["res"] == "failed":
                flag = 1
                print("DEBUG: cannot finish breaking")
    
    if nearby_block_res["y"] == str(y_height):
        sleep(1)
        if flag == 0:
            # start breaking
            start_breaking_res = mc.put_and_get("start_mine", {"x": nearby_block_res["x"], "y": str(int(nearby_block_res["y"]) + 1), "z": nearby_block_res["z"]})

        if flag == 0:
            # finish breaking
            if start_breaking_res["res"] and start_breaking_res["res"] != "0":
                time = float(start_breaking_res["res"])
                sleep(1.0 / time / 20)
                finish_breaking_res = mc.put_and_get("finish_mine", {"x": nearby_block_res["x"], "y": str(int(nearby_block_res["y"]) + 1), "z": nearby_block_res["z"]})
    
    sleep(1)
    if flag == 0:
        mc.put_and_get("move", {"x": nearby_block_res["x"], "y": str(y_height), "z": nearby_block_res["z"], "nojump": "1"})
    
    if flag == 1:
        break;
    sleep(1)