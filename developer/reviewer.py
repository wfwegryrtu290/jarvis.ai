from core.logger import logger


def has_error(result):

    if not isinstance(result, dict):

        logger.error("Invalid runner result.")

        return True

    code = result.get("returncode", -1)

    if code != 0:

        logger.error(result.get("stderr", ""))

        return True

    return False


def get_error(result):

    if not has_error(result):
        return ""

    return result.get("stderr", "").strip()


def get_output(result):

    return result.get("stdout", "").strip()
