from agents.base import BaseAgent

from tools.registry import execute


class SystemAgent(BaseAgent):

    name = "system"

    tools = [
        "computer.open",
        "terminal.run",
        "windows.open",
        "system.info",
        "computer.open",
        "computer.list",
        "computer.read",
        "terminal.run",
        "windows.open",
        "system.info"
    ]
    

    def can_handle(self, task):

        return task["agent"] == "system"

    def execute(self, task):

        return execute(

            task["tool"],

            task["arguments"]

        )


system_agent = SystemAgent()