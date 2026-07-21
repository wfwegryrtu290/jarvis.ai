import pygetwindow as gw

def get_titles():
    return gw.getAllTitles()

def activate(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:
        windows[0].activate()
        return True

    return False