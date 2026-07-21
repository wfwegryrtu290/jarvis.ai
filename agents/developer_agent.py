from agents.base import BaseAgent

from developer.agent import developer


class DeveloperAgent(BaseAgent):

    name = "developer"

    tools = [
        "developer.report",
    ]

    def can_handle(self, task):

        return task["agent"] == "developer"

    def execute(self, task):

        print("👨‍💻 Developer Agent")

        tool = task.get("tool")

        if tool == "developer.report":

            stats = developer.stats()

            report = f"""
📊 Project Report

Python files      : {stats["python_files"]}
Indexed files     : {stats["indexed_files"]}
Dependencies      : {stats["dependency_files"]}
Symbols           : {stats["symbol_files"]}
"""

            return {
                "success": True,
                "report": report
            }

        return {
            "success": False,
            "error": f"Unknown developer tool: {tool}"
        }


developer_agent = DeveloperAgent()