import pygetwindow as gw

from core.logger import logger


def get_titles():

    titles = []

    for window in gw.getAllWindows():

        title = window.title.strip()

        if title:
            titles.append(title)

    return sorted(titles)


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


def list_windows():

    return {
        "success": True,
        "report": get_titles()
    }


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

        logger.info(f"Activated window: {window.title}")

        return {
            "success": True,
            "report": f"Активирах '{window.title}'."
        }

    except Exception as e:

        logger.exception(e)

        return {
            "success": False,
            "error": str(e)
        }


def minimize(target):

    windows = _find_windows(target)

    if not windows:

        return {
            "success": False,
            "error": f"Не намерих прозорец '{target}'."
        }

    window = windows[0]

    try:

        window.minimize()

        return {
            "success": True,
            "report": f"Минимизирах '{window.title}'."
        }

    except Exception as e:

        logger.exception(e)

        return {
            "success": False,
            "error": str(e)
        }


def maximize(target):

    windows = _find_windows(target)

    if not windows:

        return {
            "success": False,
            "error": f"Не намерих прозорец '{target}'."
        }

    window = windows[0]

    try:

        window.maximize()

        return {
            "success": True,
            "report": f"Максимизирах '{window.title}'."
        }

    except Exception as e:

        logger.exception(e)

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

        logger.info(f"Closed window: {window.title}")

        return {
            "success": True,
            "report": f"Затворих '{window.title}'."
        }

    except Exception as e:

        logger.exception(e)

        return {
            "success": False,
            "error": str(e)
        }
