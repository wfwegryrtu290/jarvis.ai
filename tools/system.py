from tools.registry import register

import datetime
import platform
import socket
import getpass


@register(
    name="system.info",
    description="Връща информация за системата, часа и датата.",
    category="system",
    arguments={
        "info_type": "string"
    }
)
def system_info(arguments):

    info_type = arguments.get("info_type", "").lower()

    now = datetime.datetime.now()

    if info_type == "time":

        return {
            "success": True,
            "report": now.strftime("%H:%M:%S")
        }

    if info_type == "date":

        return {
            "success": True,
            "report": now.strftime("%d.%m.%Y")
        }

    if info_type == "datetime":

        return {
            "success": True,
            "report": now.strftime("%d.%m.%Y %H:%M:%S")
        }

    if info_type == "computer":

        return {
            "success": True,
            "report": socket.gethostname()
        }

    if info_type == "user":

        return {
            "success": True,
            "report": getpass.getuser()
        }

    if info_type == "os":

        return {
            "success": True,
            "report": f"{platform.system()} {platform.release()}"
        }

    return {
        "success": True,
        "report": {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%d.%m.%Y"),
            "computer": socket.gethostname(),
            "user": getpass.getuser(),
            "os": f"{platform.system()} {platform.release()}"
        }
    }