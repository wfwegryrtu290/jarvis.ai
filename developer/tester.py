import re


def find_traceback(stderr):

    if not stderr:
        return None

    if "Traceback" not in stderr:
        return None

    return stderr


def find_file(stderr):

    files = re.findall(r'File "(.+?)"', stderr)

    if not files:
        return None

    return files[-1]