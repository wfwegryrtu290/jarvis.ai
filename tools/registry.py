TOOLS = {}


def register(
    name,
    description="",
    category="general",
    arguments=None
):

    def decorator(func):

        TOOLS[name] = {
            "function": func,
            "description": description,
            "category": category,
            "arguments": arguments or {}
        }

        return func

    return decorator


def get_tools():

    return TOOLS


def execute(name, arguments=None):

    if name not in TOOLS:

        return {
            "success": False,
            "error": f"Unknown tool: {name}"
        }

    try:

        return TOOLS[name]["function"](arguments or {})

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }