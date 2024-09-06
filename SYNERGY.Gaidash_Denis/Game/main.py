# 🌲🌊🚁🟩🔥🏥❤🔵🏦🌥️⚡🏆⬛
from clouds import Clouds
from pynput import keyboard
from map import Map
import time
import os
from helic import Helicopter as Helic
import json


TICK_SLEEP = 0.05
TREE_UPDATE = 200
FIRE_UPDATE = 80
CLOUDS_UPDATE = 70
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
helico = Helic(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}


def ProcessKey(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    
    # Move helicopter
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.Move(dx, dy)
    # Save game
    elif c == 'f':
        data = {"helicopter": helico.ExportData(), 
                "clouds": clouds.ExportDataCloud(), 
                "field": field.ExportDataMap()}
        
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    # Load game
    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helico.ImportData(data["helicopter"])
            field.ImportData(data["field"])
            clouds.ImportData(data["clouds"]) 




listener = keyboard.Listener(
    on_press=None,
    on_release=ProcessKey)
listener.start()  

# CONFIG
while True:
    os.system("cls")
    field.ProcessHelicopter(helico, clouds)
    helico.PrintStats()
    field.PrintMap(helico, clouds)
    #print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        field.AddTree()
    if(tick % FIRE_UPDATE == 0):
        field.UpdateFires()   
    if(tick % CLOUDS_UPDATE == 0):
        clouds.UpdateClouds()   