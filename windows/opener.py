import os
import subprocess

from windows.application_scanner import scanner


def open_program(name):

    path = scanner.find(name)

    if path is None:

        return {
            "success": False,
            "error": f"Не намерих '{name}'."
        }

    os.startfile(path)

    return {
        "success": True,
        "report": f"Стартирах {name}."
    }