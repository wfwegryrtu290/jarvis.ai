from agents.base import BaseAgent
from developer.agent import developer


class DeveloperAgent(BaseAgent):

    name = "developer"

    description = "Developer Assistant"

    tools = [
        "developer.report",
        "developer.stats",
    ]

    def can_handle(self, task):

        return task.get("agent", "").lower() == "developer"

    def execute(self, task):

        print("👨‍💻 Developer Agent")

        tool = task.get("tool", "").lower()

        try:

            stats = developer.stats()

            if tool in ("developer.report", "developer.stats"):

                report = f"""
📊 Project Report

Python files      : {stats.get("python_files", 0)}
Indexed files     : {stats.get("indexed_files", 0)}
Dependencies      : {stats.get("dependency_files", 0)}
Symbols           : {stats.get("symbol_files", 0)}
"""

                return {
                    "success": True,
                    "tool": tool,
                    "stats": stats,
                    "report": report,
                }

            return {
                "success": False,
                "error": f"Unknown developer tool: {tool}"
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def status(self):

        return {
            "name": self.name,
            "description": self.description,
            "ready": True,
        }


developer_agent = DeveloperAgent()
