# Vasallius

import pyautogui

MINUTES = 10

try:
    while True:
        pyautogui.move(5, 0)
        pyautogui.sleep(60*MINUTES)
        pyautogui.move(-5, 0)
        pyautogui.sleep(60*MINUTES)
except KeyboardInterrupt:
    print('Script has terminated.')
