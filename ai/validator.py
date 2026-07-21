from agents.manager import manager
from tools.registry import get_tools


def validate(plan):

    # Планът трябва да е dict
    if not isinstance(plan, dict):
        return False, "Planner не върна валиден JSON."

    # Задължителни полета
    required = [
        "thought",
        "actions",
        "answer"
    ]

    for field in required:

        if field not in plan:
            return False, f"Липсва поле '{field}'."

    # actions трябва да е list
    if not isinstance(plan["actions"], list):
        return False, "'actions' трябва да е list."

    # Регистрирани инструменти
    tools = get_tools()

    # Регистрирани агенти
    agents = {
        agent.name: agent
        for agent in manager.agents
    }

    # Проверка на действията
    for action in plan["actions"]:

        if not isinstance(action, dict):
            return False, "Невалидно действие."

        # =====================================
        # NORMALIZATION
        # =====================================

        # Някои модели връщат tool като agent
        if action.get("agent") == "computer.open":
            action["agent"] = "system"

        if action.get("agent") == "terminal.run":
            action["agent"] = "system"

        if action.get("agent") == "windows.open":
            action["agent"] = "system"

        if action.get("agent") == "file.read":
            action["agent"] = "system"

        # computer.open използва target
        if action.get("tool") == "computer.open":

            args = action.setdefault("arguments", {})

            if "path" in args and "target" not in args:
                args["target"] = args.pop("path")

            if "name" in args and "target" not in args:
                args["target"] = args.pop("name")

        # =====================================
        # Проверки
        # =====================================

        agent_name = action.get("agent")
        tool_name = action.get("tool")
        arguments = action.get("arguments", {})

        # Проверка за агент
        if agent_name not in agents:
            return False, f"Unknown agent: {agent_name}"

        # Проверка за инструмент
        if tool_name not in tools:
            return False, f"Unknown tool: {tool_name}"

        # Инструментът трябва да принадлежи на агента
        agent = agents[agent_name]

        if tool_name not in getattr(agent, "tools", []):
            return (
                False,
                f"Tool '{tool_name}' не принадлежи на агент '{agent_name}'."
            )

        # arguments трябва да е dict
        if not isinstance(arguments, dict):
            return False, "'arguments' трябва да е dict."

    return True, None