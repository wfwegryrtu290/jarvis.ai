from typing import Any, Dict, List


class BrainAgent:
    """
    Главният агент на Jarvis.

    Получава задачи, избира кой агент да ги изпълни
    и пази текущото състояние.
    """

    name = "brain"

    def __init__(self, manager):
        self.manager = manager
        self.history: List[Dict[str, Any]] = []
        self.current_task = None

    @property
    def tools(self):
        return []

    def can_handle(self, action: Dict[str, Any]) -> bool:
        """
        Brain Agent приема всяка задача.
        """
        return True

    def execute(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Основен вход.
        """

        self.current_task = action

        self.history.append(action)

        agent_name = action.get("agent")

        if not agent_name:

            return {
                "success": False,
                "error": "Не е посочен агент."
            }

        agent = self.manager.get_agent_for_tool(agent_name)

        if agent is None:

            return {
                "success": False,
                "error": f"Агент '{agent_name}' не е намерен."
            }

        try:

            result = agent.execute(action)

            return {
                "success": True,
                "agent": agent_name,
                "result": result
            }

        except Exception as e:

            return {
                "success": False,
                "agent": agent_name,
                "error": str(e)
            }

    def get_history(self):

        return self.history

    def clear_history(self):

        self.history.clear()

    def status(self):

        return {
            "current_task": self.current_task,
            "history_size": len(self.history)
        }
