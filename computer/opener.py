import os

from computer.search import search
from context.context import context


def open_target(target):

    result = search(target)

    if result is None:

        return {
            "success": False,
            "error": f"Не намерих '{target}'."
        }

    kind, path = result

    # Запомняме последното отворено
    if kind == "folder":
        context.current_folder = path

    elif kind == "file":
        context.current_file = path

    elif kind == "app":
        context.current_app = path

    try:

        os.startfile(path)

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    return {

        "success": True,

        "message": f"Отворих {target}.",

        "kind": kind,

        "path": path

    }
