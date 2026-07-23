from ai.intent import resolve
from tools.registry import execute


def run(plan):

    # Ако някой е подал директно текстова команда,
    # първо опитай локално разпознаване.
    if isinstance(plan, str):

        intent = resolve(plan)

        if intent.get("handled"):

            plan = intent["plan"]

        else:

            return []

    actions = plan.get("actions", [])

    results = []

    for action in actions:

        tool = action.get("tool")

        arguments = action.get("arguments", {})

        result = execute(tool, arguments)

        results.append(result)

        # Спира при грешка
        if isinstance(result, dict):

            if result.get("success") is False:

                break

    return results
