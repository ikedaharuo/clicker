import math
import pyautogui
import time
import random

def auto_click(interval, clicks):
    print("Auto Clicker started. Press Ctrl+C to stop.")
    last_x, last_y = pyautogui.position()
    stationary_x, stationary_y = None, None
    try:
        for _ in range(clicks):
            current_x, current_y = pyautogui.position()
            if current_x != last_x or current_y != last_y:
                print("Mouse is moving. Waiting for it to stop...")
                print(f"{current_x}, {current_y}")
                print(f"{stationary_x}, {stationary_y}")
                time.sleep(random.uniform(0.00001, 0.0001))
                if stationary_x is None and stationary_y is None:
                    stationary_x, stationary_y = pyautogui.position()
                elif (current_x not in [x for x in range(current_x-20, current_x+20)] or current_y  not in [y for y in range(current_y-20, current_y+20)]):
                    stationary_x, stationary_y = pyautogui.position()

            else:
                print("Mouse is stationary. Clicking...")
                if stationary_x is not None and stationary_y is not None:
                    offset_x = random.randint(-20, 20)
                    offset_y = random.randint(-20, 20)
                    pyautogui.click(x=stationary_x + offset_x, y=stationary_y + offset_y, button='left')
                else:
                    pyautogui.click(button='left')
            last_x, last_y = current_x, current_y
    except KeyboardInterrupt:
        print("\nAuto Clicker stopped.")

if __name__ == "__main__":
    try:
        while True:
            auto_click(0.001, 10000)
            pyautogui.press('f5')
            time.sleep(random.randint(0.01, 0.1))
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")
