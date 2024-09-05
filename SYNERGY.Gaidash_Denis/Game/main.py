# 🌲🌊🚁🟩🔥🏥💌🫗🏦🌥️⚡🏆⬛

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
#field.PrintMap()

helico = Helic(MAP_W, MAP_H)

tick = 1  

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()  

while True:
    os.system("cls")
    print("TICK", tick)
    field.PrintMap(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        field.AddTree()
    if(tick % FIRE_UPDATE == 0):
        field.UpdateFires()      