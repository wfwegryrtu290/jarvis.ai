from agents.base import BaseAgent


class FileAgent(BaseAgent):

    name = "file"

    tools = [
        "file.read",
        "file.write",
        "file.list",
    ]

    def can_handle(self, task):

        return task["agent"] == "file"

    def execute(self, task):

        return {
            "success": True
        }


file_agent = FileAgent()