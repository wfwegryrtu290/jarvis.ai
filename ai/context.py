from developer.agent import developer
from agents.manager import manager
from tools.registry import get_tools
from memory.manager import memory


def build_context():

    # ==========================
    # Project
    # ==========================

    project = developer.stats()

    # ==========================
    # Agents
    # ==========================

    agent_list = []

    for agent in manager.agents:

        agent_list.append(f"- {agent.name}")

        for tool in getattr(agent, "tools", []):

            agent_list.append(f"    • {tool}")

    # ==========================
    # Tools
    # ==========================

    tool_list = []

    for name, tool in get_tools().items():

        description = tool.get(
            "description",
            ""
        )

        tool_list.append(
            f"- {name}: {description}"
        )

    # ==========================
    # Memory
    # ==========================

    memory_context = memory.context(10)

    if not memory_context:

        memory_context = "Няма предишни разговори."

    # ==========================
    # Build
    # ==========================

    return f"""
================ PROJECT ================

{project}

================ AGENTS ================

{chr(10).join(agent_list)}

================ TOOLS ================

{chr(10).join(tool_list)}

================ MEMORY ================

{memory_context}

========================================
"""
