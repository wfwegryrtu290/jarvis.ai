import pyautogui

def screenshot(path="screen.png"):
    pyautogui.screenshot(path)
    return path