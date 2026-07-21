from tools.registry import execute


def run(plan):

    results = []

    actions = plan.get("actions", [])

    for action in actions:

        tool = action.get("tool")

        arguments = action.get("arguments", {})

        result = execute(tool, arguments)

        results.append(result)

    return results