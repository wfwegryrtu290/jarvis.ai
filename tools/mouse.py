import pyautogui


def move(x, y):

    pyautogui.moveTo(
        x,
        y
    )

    return f"Мишката е преместена на {x},{y}"


def click():

    pyautogui.click()

    return "Кликнато."