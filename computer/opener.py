import os

from computer.history import history
from computer.search import search


def open_target(target):

    result = search(target)

    if result is None:

        return {
            "success": False,
            "error": f"Не намерих '{target}'."
        }

    kind, path = result

    history.remember(kind, path)

    os.startfile(path)

    return {

        "success": True,

        "report": f"Отворих {target}.",

        "type": kind,

        "path": path

    }