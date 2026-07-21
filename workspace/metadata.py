import os
import hashlib
from workspace.classifier import get_type


def get_metadata(path):

    stat = os.stat(path)

    return {

        "name": os.path.basename(path),

        "path": path,

        "size": stat.st_size,

        "type": get_type(path),

        "modified": stat.st_mtime,

        "extension": os.path.splitext(path)[1].lower()

    }