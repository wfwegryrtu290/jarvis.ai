import shutil
import os
from datetime import datetime


BACKUP_DIR = "backups"


def backup(path):

    os.makedirs(BACKUP_DIR, exist_ok=True)

    filename = os.path.basename(path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    destination = os.path.join(
        BACKUP_DIR,
        f"{timestamp}_{filename}"
    )

    shutil.copy2(path, destination)

    return destination