from tools.registry import register
from windows.opener import open_program


@register(
    name="windows.open",
    description="Отваря инсталирано приложение",
    category="system",
    arguments={
        "program": "string"
    }
)
def windows_open(args):

    return open_program(args["program"])