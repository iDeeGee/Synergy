# 🌲🌊🚁🟩🔥🏥💌🫗🏦🌥️⚡🏆⬛

from map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 25
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.GenerateForest(3,10) # 3,10
field.GenerateRiver(10)
field.GenerateRiver(10)
field.GenerateRiver(10)
field.PrintMap()

tick = 1

while True:
    os.system("cls")
    print("TICK", tick)
    field.PrintMap()
    tick += 1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        field.AddTree()
    if(tick % FIRE_UPDATE == 0):
        field.AddFire()        