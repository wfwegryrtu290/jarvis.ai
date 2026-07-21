class AgentManager:

    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def get_agent_for_tool(self, tool_name):

        for agent in self.agents:

            if tool_name in getattr(agent, "tools", []):
                return agent.name

        return None

    def execute(self, action):

        for agent in self.agents:

            if agent.can_handle(action):
                return agent.execute(action)

        return {
            "success": False,
            "error": f"Няма агент за '{action.get('agent')}'."
        }


manager = AgentManager()