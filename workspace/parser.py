import ast


def parse_python(path):

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    tree = ast.parse(code)

    data = {

        "functions": [],

        "classes": [],

        "imports": []

    }

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            data["functions"].append({

                "name": node.name,

                "line": node.lineno

            })

        elif isinstance(node, ast.ClassDef):

            data["classes"].append({

                "name": node.name,

                "line": node.lineno

            })

        elif isinstance(node, ast.Import):

            for n in node.names:

                data["imports"].append(n.name)

        elif isinstance(node, ast.ImportFrom):

            if node.module:

                data["imports"].append(node.module)

    return data