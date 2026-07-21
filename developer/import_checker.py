import subprocess


def run_project():

    result = subprocess.run(
        ["python", "main.py"],
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr
    }