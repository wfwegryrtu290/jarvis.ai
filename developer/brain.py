from developer.coder import generate_patch

from workspace.patcher import patch


def improve(path, task):

    print("🤖 Анализирам проекта...")

    code = generate_patch(task)

    print("✅ Генериран е нов код.")

    result = patch(

        path,

        code

    )

    return result