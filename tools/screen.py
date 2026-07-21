import pyautogui


def capture():

    image = pyautogui.screenshot()

    path = "screen.png"

    image.save(path)

    return path