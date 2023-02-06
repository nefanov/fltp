import clang.cindex as clci
import sys, os

function_calls = []
function_declarations = []
def traverse(node):

    for child in node.get_children():
        traverse(child)

    if node.kind == clci.CursorKind.CALL_EXPR:
        function_calls.append(node)

    if node.kind == clci.CursorKind.FUNCTION_DECL:
        function_declarations.append(node)


    print('Found %s [line=%s, col=%s]' % (node.displayname, node.location.line, node.location.column))

clci.Config.set_library_path("C:\lib") # place your libclang.dll there (as you see, I examined this example under Windows)
index = clci.Index.create()
# print(os.getcwd())
fn = "1.ast" if len(sys.argv)<2 else sys.argv[0]
tu = index.parse(fn)
root = tu.cursor
traverse(root)
