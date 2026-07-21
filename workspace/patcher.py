from workspace.backup import backup
from workspace.writer import write_file


def patch(path, new_content):

    backup_file = backup(path)

    result = write_file(path, new_content)

    return {

        "backup": backup_file,

        "result": result

    }