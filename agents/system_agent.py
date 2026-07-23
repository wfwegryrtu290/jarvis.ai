from agents.base import BaseAgent

from tools.registry import execute


class SystemAgent(BaseAgent):

    name = "system"

    tools = [

        "computer.open",
        "computer.list",
        "computer.read",
        "computer.activate",
        "computer.close",

        "terminal.run",

        "windows.open",

        "system.info"

    ]

    def can_handle(self, task):

        return task.get("agent") == "system"

    def execute(self, task):

        tool = task.get("tool")

        if tool not in self.tools:

            return {
                "success": False,
                "error": f"Tool '{tool}' не принадлежи на агент '{self.name}'."
            }

        return execute(

            tool,

            task.get("arguments", {})

        )


system_agent = SystemAgent()
