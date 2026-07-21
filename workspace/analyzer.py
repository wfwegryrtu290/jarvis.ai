import ast


def analyze(path):

    with open(path, "r", encoding="utf-8") as f:

        tree = ast.parse(f.read())

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):

            classes.append(node.name)

        elif isinstance(node, ast.Import):

            for item in node.names:

                imports.append(item.name)

        elif isinstance(node, ast.ImportFrom):

            imports.append(node.module)

    return {

        "functions": functions,

        "classes": classes,

        "imports": imports

    }