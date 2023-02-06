class Node:
    def __init__(self):
        self.opnds = []

    def accept(self, visitor):
        visitor.visit(self)

    def dumpName(self):
        print(self, self.name)

    def __str__(self):
        return self.__class__.__name__

class TransUnitNode(Node):
    name = "proga:"
    pass

class VarNode(Node):
    name = "v"
    val = 5
    pass

class StrConstNode(Node):
    name = "Hello"
    pass

class NumConstNode(Node):
    name = 5
    pass

class OpNode(Node):
    name = "OP_repeat"
    arity = 2
    pass


""" Abstract Visitor class for Concrete Visitor classes:
 method defined in this class will be inherited by all
 Concrete Visitor classes."""
class Visitor:
    def __str__(self):
        return self.__class__.__name__

""" Concrete Visitors: Classes visiting Concrete objects. """
class DumpVisitor(Visitor):
    def visit(self, instance):
        print(instance.__class__)
        instance.dumpName()

"""creating objects for concrete classes, make a tree from them"""
program = TransUnitNode()
op1 = OpNode()
operand1 = StrConstNode()
operand2 = NumConstNode()
program.opnds.append(op1)
op1.opnds.append(operand1)
op1.opnds.append(operand2)

def traverse(node, operator):
    if (node):
        node.accept(operator)
        if len(node.opnds) > 0:
            for child in node.opnds:
                traverse(child, operator)
    return

"""Creating Visitors"""
dumper = DumpVisitor()

"""Visitors visiting courses"""
traverse(program, dumper)
