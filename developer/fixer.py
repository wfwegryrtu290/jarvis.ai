from developer.coder import improve
from developer.backup import backup
from developer.memory import save


def fix(file, error):

    with open(file, "r", encoding="utf-8") as f:

        code = f.read()

    backup(file)

    new_code = improve(code, error)

    with open(file, "w", encoding="utf-8") as f:

        f.write(new_code)

    save(

        file,

        error,

        "automatic",

        1

    )

    return True