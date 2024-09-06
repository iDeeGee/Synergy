# 🌲🌊🚁🟩🔥🏥💌🔵🏦🌥️⚡🏆⬛

from pynput import keyboard
from map import Map
import time
import os
from helic import Helicopter as Helic



TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.GenerateForest(3,10) # 3,10
field.GenerateRiver(10)
field.GenerateRiver(10)
field.GenerateRiver(10)
field.UpgradeShop()
#field.PrintMap()

helico = Helic(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def ProcessKey(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.Move(dx, dy)

        

listener = keyboard.Listener(
    on_press=None,
    on_release=ProcessKey)
listener.start()  


tick = 1  

# CONFIG
while True:
    os.system("cls")
    #print("TICK", tick)
    field.ProcessHelicopter(helico)
    helico.PrintStats()
    field.PrintMap(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        field.AddTree()
    if(tick % FIRE_UPDATE == 0):
        field.UpdateFires()      