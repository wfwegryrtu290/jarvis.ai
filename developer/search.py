from core.logger import logger
from developer.context import context


def find_function(name):

    if not name:
        return []

    name = name.strip()

    logger.debug(f"Searching function: {name}")

    result = []

    for file, functions in context.functions.items():

        if name in functions:
            result.append(file)

    return sorted(result)


def find_import(module):

    if not module:
        return []

    module = module.strip()

    logger.debug(f"Searching import: {module}")

    result = []

    for file, imports in context.imports.items():

        if module in imports:
            result.append(file)

    return sorted(result)


def find_class(name):

    if not name:
        return []

    name = name.strip()

    logger.debug(f"Searching class: {name}")

    result = []

    for file, classes in context.classes.items():

        if name in classes:
            result.append(file)

    return sorted(result)
