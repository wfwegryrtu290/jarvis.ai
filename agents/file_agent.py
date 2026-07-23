from pathlib import Path

from agents.base import BaseAgent


class FileAgent(BaseAgent):

    name = "file"

    tools = [
        "file.read",
        "file.write",
        "file.list",
        "file.exists",
    ]

    def can_handle(self, task):

        return task.get("agent", "").lower() == "file"

    def execute(self, task):

        command = task.get("command", "").lower()

        if command == "read":
            return self.read_file(task.get("path"))

        if command == "write":
            return self.write_file(
                task.get("path"),
                task.get("content", "")
            )

        if command == "list":
            return self.list_files(task.get("path", "."))

        if command == "exists":
            path = Path(task.get("path", ""))

            return {
                "success": True,
                "exists": path.exists()
            }

        return {
            "success": False,
            "error": "Непозната команда."
        }

    def read_file(self, filename):

        try:

            path = Path(filename)

            text = path.read_text(
                encoding="utf-8"
            )

            return {
                "success": True,
                "content": text
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def write_file(self, filename, content):

        try:

            path = Path(filename)

            path.write_text(
                content,
                encoding="utf-8"
            )

            return {
                "success": True
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def list_files(self, folder):

        try:

            path = Path(folder)

            files = [
                p.name
                for p in path.iterdir()
            ]

            return {
                "success": True,
                "files": sorted(files)
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


file_agent = FileAgent()
