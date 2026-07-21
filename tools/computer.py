from tools.registry import register

from computer.opener import open_target
from computer.lister import list_folder
from computer.reader import read_file

print("✅ computer tool loaded")


@register(
    name="computer.open",
    description="Отваря приложение, файл или папка.",
    category="system",
    arguments={
        "target": "string"
    }
)
def computer_open(arguments):

    return open_target(
        arguments["target"]
    )


@register(
    name="computer.list",
    description="Показва съдържанието на папка.",
    category="system",
    arguments={
        "target": "string"
    }
)
def computer_list(arguments):

    return list_folder(
        arguments.get("target")
    )


@register(
    name="computer.read",
    description="Чете файл.",
    category="system",
    arguments={
        "target": "string"
    }
)
def computer_read(arguments):

    return read_file(
        arguments.get("target")
    )