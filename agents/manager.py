from core.logger import logger


class AgentManager:

    def __init__(self):

        self.agents = []

    def register(self, agent):

        if agent in self.agents:
            return

        logger.info(f"Registered agent: {agent.name}")

        self.agents.append(agent)

    def unregister(self, name):

        self.agents = [
            agent
            for agent in self.agents
            if getattr(agent, "name", "").lower() != name.lower()
        ]

        logger.info(f"Unregistered agent: {name}")

    def clear(self):

        self.agents.clear()

    def list_agents(self):

        return [
            getattr(agent, "name", agent.__class__.__name__)
            for agent in self.agents
        ]

    def get(self, name):

        for agent in self.agents:

            if getattr(agent, "name", "").lower() == name.lower():
                return agent

        return None

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

        if not isinstance(action, dict):

            return {
                "success": False,
                "error": "Невалидно действие."
            }

        logger.info(f"Executing: {action}")

        for agent in self.agents:

            try:

                if agent.can_handle(action):

                    result = agent.execute(action)

                    logger.debug(result)

                    return result

            except Exception as e:

                logger.exception(e)

                return {
                    "success": False,
                    "agent": getattr(agent, "name", "unknown"),
                    "error": str(e)
                }

        return {
            "success": False,
            "error": f"Няма агент за '{action.get('agent', 'unknown')}'."
        }


manager = AgentManager()
