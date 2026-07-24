import os
import shutil
from datetime import datetime

from core.logger import logger


BACKUP_FOLDER = "backups"


def backup(file):

    if not os.path.exists(file):

        raise FileNotFoundError(file)

    os.makedirs(
        BACKUP_FOLDER,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = os.path.basename(file)

    name, ext = os.path.splitext(filename)

    dst = os.path.join(
        BACKUP_FOLDER,
        f"{name}_{timestamp}{ext}"
    )

    shutil.copy2(file, dst)

    logger.info(f"Backup created: {dst}")

    return dst
