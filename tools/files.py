from tools.registry import register


@register(
    name="file.read",
    description="Прочита текстов файл",
    category="file",
    arguments={
        "path": "string"
    }
)
def read(arguments):

    path = arguments.get("path")

    if not path:
        return {
            "success": False,
            "error": "Липсва път до файла."
        }

    try:

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

        return {
            "success": True,
            "content": text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }