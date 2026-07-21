import ast


class CallVisitor(ast.NodeVisitor):

    def __init__(self):

        self.calls = []

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            self.calls.append(node.func.id)

        self.generic_visit(node)