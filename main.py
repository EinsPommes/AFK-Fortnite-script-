import pyautogui
import random
import time
import keyboard

def move_mouse_randomly():
    x, y = pyautogui.size()
    new_x = random.randint(0, x)
    new_y = random.randint(0, y)
    pyautogui.moveTo(new_x, new_y, duration=random.uniform(0.1, 1.0))

def press_wasd_randomly():
    keys = ['w', 'a', 's', 'd']
    key = random.choice(keys)
    keyboard.press(key)
    time.sleep(random.uniform(0.2, 0.5))
    keyboard.release(key)

try:
    print("Starte AFK-Farming Script. Drücke STRG+C, um es zu beenden.")
    while True:
        move_mouse_randomly()
        time.sleep(random.uniform(5, 10))
        press_wasd_randomly()
        time.sleep(random.uniform(5, 10))

except KeyboardInterrupt:
    print("Script beendet.")
