from tools.registry import register

from developer.checker import check
from developer.report import create_report


@register(
    name="developer.report",
    description="Генерира отчет за проекта."
)
def developer_report(arguments):

    result = check(".")

    return {
        "success": result["success"],
        "report": create_report(result)
    }