class AgentManager:

    def __init__(self):
        self.agents = []

    def register(self, agent):
        """
        Регистрира агент, ако вече не е добавен.
        """

        if agent not in self.agents:
            self.agents.append(agent)

    def unregister(self, name):
        """
        Премахва агент по име.
        """

        self.agents = [
            agent
            for agent in self.agents
            if getattr(agent, "name", "").lower() != name.lower()
        ]

    def list_agents(self):
        """
        Връща списък с имената на всички агенти.
        """

        return [
            getattr(agent, "name", agent.__class__.__name__)
            for agent in self.agents
        ]

    def get_agent_for_tool(self, tool_name):

        tool_name = tool_name.lower()

        for agent in self.agents:

            tools = [
                tool.lower()
                for tool in getattr(agent, "tools", [])
            ]

            if tool_name in tools:
                return agent.name

        return None

    def execute(self, action):

        for agent in self.agents:

            try:

                if agent.can_handle(action):
                    return agent.execute(action)

            except Exception as e:

                return {
                    "success": False,
                    "error": str(e),
                    "agent": getattr(agent, "name", "unknown")
                }

        return {
            "success": False,
            "error": f"Няма агент за '{action.get('agent', 'unknown')}'."
        }


manager = AgentManager()
