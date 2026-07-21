def has_error(result):

    if result["returncode"] != 0:

        return True

    return False