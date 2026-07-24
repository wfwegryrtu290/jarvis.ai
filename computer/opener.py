import os
import webbrowser
from pathlib import Path

from core.logger import logger
from computer.search import search
from context.context import context


def open_target(target):

    if not target:

        return {
            "success": False,
            "error": "Не е подаден обект за отваряне."
        }

    target = str(target).strip()

    logger.info(f"Open request: {target}")

    # ==========================
    # URL
    # ==========================

    if target.startswith(("http://", "https://")):

        try:

            webbrowser.open(target)

            return {
                "success": True,
                "message": f"Отворих {target}.",
                "kind": "url",
                "path": target
            }

        except Exception as e:

            logger.exception(e)

            return {
                "success": False,
                "error": str(e)
            }

    # ==========================
    # Search
    # ==========================

    result = search(target)

    if result is None:

        logger.warning(f"Not found: {target}")

        return {
            "success": False,
            "error": f"Не намерих '{target}'."
        }

    kind, path = result

    path = str(Path(path))

    # ==========================
    # Context
    # ==========================

    if kind == "folder":
        context.current_folder = path

    elif kind == "file":
        context.current_file = path

    elif kind == "app":
        context.current_app = path

    # ==========================
    # Open
    # ==========================

    try:

        os.startfile(path)

        logger.info(f"Opened {kind}: {path}")

    except Exception as e:

        logger.exception(e)

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
