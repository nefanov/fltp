import ast


class MyVisitor(ast.NodeVisitor):
    def visit_Name(self, node): print('content\n\tName:', node.id)
    def generic_visit(self, node):
        print('--')
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

x = MyVisitor()

x.visit(ast.parse('f"sin({a}) is {sin(a):.3}"', mode='eval'))
