import os
import py_compile


def check(root="."):

    report = {
        "success": True,
        "files": 0,
        "errors": []
    }

    for current, dirs, files in os.walk(root):

        dirs[:] = [

            d for d in dirs

            if d not in (
                "__pycache__",
                ".git",
                ".venv",
                "venv"
            )
        ]

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(current, file)

            report["files"] += 1

            try:

                py_compile.compile(
                    path,
                    doraise=True
                )

            except Exception as e:

                report["success"] = False

                report["errors"].append({

                    "file": path,

                    "error": str(e)

                })

    return report