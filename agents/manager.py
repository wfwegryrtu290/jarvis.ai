from __future__ import annotations

from typing import Any


class AgentManager:
    """
    Централен мениджър на всички агенти.
    """

    def __init__(self) -> None:
        self._agents: dict[str, Any] = {}

    def register(self, agent: Any) -> None:
        """
        Регистрира нов агент.
        """

        name = getattr(agent, "name", agent.__class__.__name__).lower()

        self._agents[name] = agent

    def unregister(self, name: str) -> bool:
        """
        Премахва агент.
        """

        name = name.lower()

        if name in self._agents:
            del self._agents[name]
            return True

        return False

    def get(self, name: str):
        """
        Връща агент по име.
        """

        return self._agents.get(name.lower())

    def list_agents(self) -> list[str]:
        """
        Списък на всички агенти.
        """

        return sorted(self._agents.keys())

    def get_agent_for_tool(self, tool_name: str):
        """
        Намира кой агент може да използва даден инструмент.
        """

        tool_name = tool_name.lower()

        for agent in self._agents.values():

            tools = [
                t.lower()
                for t in getattr(agent, "tools", [])
            ]

            if tool_name in tools:
                return agent

        return None

    def execute(self, action: dict):
        """
        Изпълнява задача чрез подходящ агент.
        """

        agent_name = action.get("agent")

        if agent_name:

            agent = self.get(agent_name)

            if agent is None:
                return {
                    "success": False,
                    "error": f"Агент '{agent_name}' не е намерен."
                }

            return agent.execute(action)

        for agent in self._agents.values():

            if hasattr(agent, "can_handle") and agent.can_handle(action):
                return agent.execute(action)

        return {
            "success": False,
            "error": "Няма подходящ агент."
        }

    def stats(self) -> dict:
        """
        Статистика за Dashboard.
        """

        return {
            "agents": len(self._agents),
            "names": self.list_agents(),
        }


manager = AgentManager()
