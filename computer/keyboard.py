import pyautogui

def write(text):
    pyautogui.write(text, interval=0.01)

def press(key):
    pyautogui.press(key)

def hotkey(*keys):
    pyautogui.hotkey(*keys)