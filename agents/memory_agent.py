from typing import Any, Dict, List

from agents.base import BaseAgent


class MemoryAgent(BaseAgent):
    """
    Memory Agent

    Управлява краткосрочната памет на Jarvis.
    По-късно ще бъде разширен с ChromaDB/SQLite.
    """

    name = "memory"

    tools = [
        "memory",
        "remember",
        "recall",
        "forget",
    ]

    def __init__(self):
        self.memory: List[Dict[str, Any]] = []

    def can_handle(self, action: Dict[str, Any]) -> bool:
        agent = action.get("agent", "").lower()
        return agent == "memory"

    def execute(self, action: Dict[str, Any]) -> Dict[str, Any]:

        command = action.get("command", "remember").lower()

        if command == "remember":

            item = action.get("data")

            if item is None:
                return {
                    "success": False,
                    "error": "Няма данни за запомняне."
                }

            self.memory.append(item)

            return {
                "success": True,
                "message": "Информацията е запомнена.",
                "count": len(self.memory)
            }

        if command == "recall":

            return {
                "success": True,
                "memory": self.memory
            }

        if command == "forget":

            self.memory.clear()

            return {
                "success": True,
                "message": "Паметта е изчистена."
            }

        return {
            "success": False,
            "error": "Непозната команда."
        }

    def status(self):

        return {
            "items": len(self.memory)
        }


memory_agent = MemoryAgent()
