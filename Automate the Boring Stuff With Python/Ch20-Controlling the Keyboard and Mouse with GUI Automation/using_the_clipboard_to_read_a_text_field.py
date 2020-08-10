# Using the Clipboard to Read a Text Field

import pyautogui
import pyperclip

# Get notepad window and make it active
notepad_window = pyautogui.getWindowsWithTitle('Notepad')
notepad_window[0].activate()

# Get notepad content into clipboard
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

print(pyperclip.paste())
