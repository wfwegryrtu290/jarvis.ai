import subprocess


def run_python(file):

    result = subprocess.run(

        ["python", file],

        capture_output=True,

        text=True

    )

    return {

        "stdout": result.stdout,

        "stderr": result.stderr,

        "returncode": result.returncode

    }