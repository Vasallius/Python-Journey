# Instant Messenger Bot

import pyautogui

# Messenger was my preffered chat platform
m = pyautogui.getWindowsWithTitle('messenger - google chrome')
m[0].activate()

# Insert name of friends
friends = ['friend A', 'friend B']


def send_message(name):
    pyautogui.click((306, 133))
    pyautogui.sleep(1)
    pyautogui.write(name)
    pyautogui.sleep(2)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(
        f'Hi {name}. Sorry for receiving this message. I\'m testing message automation.')
    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(1)


# Send the message
for friend in friends:
    send_message(friend)
