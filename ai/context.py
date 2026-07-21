from developer.agent import developer
from agents.manager import manager
from tools.registry import get_tools


def build_context():

    tools = get_tools()

    tool_list = ""

    for name, tool in tools.items():
        tool_list += f"- {name}: {tool['description']}\n"

    agent_list = ""

    for agent in manager.agents:

        agent_list += f"\n{agent.name}\n"

        for tool in getattr(agent, "tools", []):
            agent_list += f"  - {tool}\n"

    return f"""
===== PROJECT =====

{developer.stats()}

===== AGENTS =====

{agent_list}

===== TOOLS =====

{tool_list}
"""