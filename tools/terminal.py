import subprocess

from tools.registry import register


@register(
    name="terminal.run",
    description="Изпълнява команда в терминала",
    category="system",
    arguments={
        "command": "string"
    }
)
def run(arguments):

    command = arguments.get("command")

    if not command:
        return {
            "success": False,
            "error": "Няма команда."
        }

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "code": result.returncode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }