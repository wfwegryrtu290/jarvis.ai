import pygetwindow as gw


def get_titles():

    titles = []

    for window in gw.getAllWindows():

        title = window.title.strip()

        if title:

            titles.append(title)

    return titles


def _find_windows(target):

    target = target.lower().strip()

    matches = []

    for window in gw.getAllWindows():

        title = window.title.strip()

        if not title:
            continue

        if target in title.lower():

            matches.append(window)

    return matches


def activate(target):

    windows = _find_windows(target)

    if not windows:

        return {
            "success": False,
            "error": f"Не намерих прозорец '{target}'."
        }

    if len(windows) > 1:

        return {
            "success": False,
            "error": "Намерени са няколко прозореца.",
            "windows": [w.title for w in windows]
        }

    window = windows[0]

    try:

        if window.isMinimized:
            window.restore()

        window.activate()

        return {

            "success": True,

            "report": f"Активирах '{window.title}'."

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }


def close(target):

    windows = _find_windows(target)

    if not windows:

        return {
            "success": False,
            "error": f"Не намерих прозорец '{target}'."
        }

    if len(windows) > 1:

        return {
            "success": False,
            "error": "Намерени са няколко прозореца.",
            "windows": [w.title for w in windows]
        }

    window = windows[0]

    try:

        window.close()

        return {

            "success": True,

            "report": f"Затворих '{window.title}'."

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
