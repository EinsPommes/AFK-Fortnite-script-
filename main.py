

import pyautogui
import random
import time
import keyboard


MOUSE_MOVE_INTERVAL = (5, 10)
WASD_PRESS_INTERVAL = (5, 10)
MOUSE_MOVE_DURATION = (0.1, 1.0)
WASD_PRESS_DURATION = (0.2, 0.5)

def move_mouse_randomly():
    x, y = pyautogui.size()
    new_x = random.randint(0, x - 1)
    new_y = random.randint(0, y - 1)
    pyautogui.moveTo(new_x, new_y, duration=random.uniform(*MOUSE_MOVE_DURATION))

def press_wasd_randomly():
    keys = ['w', 'a', 's', 'd']
    key = random.choice(keys)
    keyboard.press(key)
    time.sleep(random.uniform(*WASD_PRESS_DURATION))
    keyboard.release(key)

if __name__ == "__main__":
    try:
        print("Starte AFK-Farming Script. Drücke STRG+C, um es zu beenden.")
        while True:
            move_mouse_randomly()
            time.sleep(random.uniform(*MOUSE_MOVE_INTERVAL))
            press_wasd_randomly()
            time.sleep(random.uniform(*WASD_PRESS_INTERVAL))
    except KeyboardInterrupt:
        print("Script beendet.")
