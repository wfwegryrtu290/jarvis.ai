import shutil
import os


BACKUP_FOLDER = "backups"


def backup(file):

    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    filename = os.path.basename(file)

    dst = os.path.join(BACKUP_FOLDER, filename)

    shutil.copy(file, dst)

    return dst