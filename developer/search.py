from developer.context import context


def find_function(name):

    result = []

    for file, funcs in context.functions.items():

        if name in funcs:

            result.append(file)

    return result


def find_import(module):

    result = []

    for file, imports in context.imports.items():

        if module in imports:

            result.append(file)

    return result