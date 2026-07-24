import subprocess

from core.logger import logger


def run_python(file):

    try:

        result = subprocess.run(
            ["python", file],
            capture_output=True,
            text=True,
            timeout=60
        )

        success = result.returncode == 0

        if success:
            logger.info(f"Executed: {file}")
        else:
            logger.error(f"Execution failed: {file}")

        return {
            "success": success,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except subprocess.TimeoutExpired:

        logger.error(f"Timeout while executing {file}")

        return {
            "success": False,
            "stdout": "",
            "stderr": "Execution timed out.",
            "returncode": -1
        }

    except Exception as e:

        logger.exception(e)

        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1
        }
