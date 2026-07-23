from agents.manager import manager
from tools.registry import get_tools

MAX_ACTIONS = 50


def normalize_action(action):

    agent = str(action.get("agent", "")).lower()
    tool = str(action.get("tool", "")).lower()

    action["agent"] = agent
    action["tool"] = tool

    mapping = {
        "computer.open": "system",
        "terminal.run": "system",
        "windows.open": "system",
        "file.read": "system",
    }

    if agent in mapping:
        action["agent"] = mapping[agent]

    if tool == "computer.open":

        args = action.setdefault("arguments", {})

        if "path" in args and "target" not in args:
            args["target"] = args.pop("path")

        if "name" in args and "target" not in args:
            args["target"] = args.pop("name")


def validate(plan):

    if not isinstance(plan, dict):
        return False, "Planner не върна валиден JSON."

    required = [
        "thought",
        "actions",
        "answer"
    ]

    for field in required:

        if field not in plan:
            return False, f"Липсва поле '{field}'."

    if not isinstance(plan["thought"], str):
        return False, "'thought' трябва да е string."

    if not isinstance(plan["answer"], str):
        return False, "'answer' трябва да е string."

    if not isinstance(plan["actions"], list):
        return False, "'actions' трябва да е list."

    if len(plan["actions"]) > MAX_ACTIONS:
        return False, f"Планът съдържа повече от {MAX_ACTIONS} действия."

    tools = get_tools()

    agents = {
        agent.name.lower(): agent
        for agent in manager.agents
    }

    for action in plan["actions"]:

        if not isinstance(action, dict):
            return False, "Невалидно действие."

        normalize_action(action)

        required_action = [
            "agent",
            "tool",
            "arguments"
        ]

        for field in required_action:

            if field not in action:
                return False, f"Липсва поле '{field}' в действие."

        agent_name = action["agent"]
        tool_name = action["tool"]
        arguments = action["arguments"]

        if agent_name not in agents:
            return False, f"Unknown agent: {agent_name}"

        if tool_name not in tools:
            return False, f"Unknown tool: {tool_name}"

        if not isinstance(arguments, dict):
            return False, "'arguments' трябва да е dict."

        agent = agents[agent_name]

        if tool_name not in getattr(agent, "tools", []):
            return (
                False,
                f"Tool '{tool_name}' не принадлежи на агент '{agent_name}'."
            )

        # =====================================
        # Security Layer (v1)
        # =====================================

        dangerous = (
            "format",
            "shutdown",
            "restart",
            "del ",
            "rm -rf",
            "powershell",
        )

        for value in arguments.values():

            if not isinstance(value, str):
                continue

            text = value.lower()

            for command in dangerous:

                if command in text:

                    return (
                        False,
                        f"Опасна команда: {command}"
                    )

    return True, None
