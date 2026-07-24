from core.logger import logger


def replace_text(file, old, new):

    if not old:
        return False

    try:

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

    except Exception as e:

        logger.exception(e)

        return False

    if old not in text:

        logger.warning(f"Text not found in {file}")

        return False

    count = text.count(old)

    text = text.replace(old, new)

    try:

        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

    except Exception as e:

        logger.exception(e)

        return False

    logger.info(
        f"Patched '{file}' ({count} replacement{'s' if count != 1 else ''})"
    )

    return True
