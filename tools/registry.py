TOOLS = {}


def register(
    name,
    description="",
    category="general",
    arguments=None,
):

    def decorator(func):

        TOOLS[name] = {
            "function": func,
            "description": description,
            "category": category,
            "arguments": arguments or {},
        }

        return func

    return decorator


def get_tools():

    return TOOLS


def execute(name, arguments=None):

    tool = TOOLS.get(name)

    if tool is None:

        return {
            "success": False,
            "error": f"Unknown tool: {name}",
        }

    if arguments is None:
        arguments = {}

    try:

        # Ако arguments не е речник
        if not isinstance(arguments, dict):
            arguments = {}

        return tool["function"](**arguments)

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
        }


def exists(name):

    return name in TOOLS


def list_tools():

    return list(TOOLS.keys())


def info(name):

    return TOOLS.get(name)
