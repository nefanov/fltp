import json
import pydot
import sys

filename = sys.argv[1] if len(sys.argv)>1 else 'test.json'
with open(filename, 'r') as f:
    data = json.load(f)
print(data)

graph = pydot.Dot('my_graph', graph_type='digraph', rankdir='LR')

graph.add_node(pydot.Node('\2', shape='point'))
for state in data['states']:
    if state not in data['final_states']:
        graph.add_node(pydot.Node(state, shape='circle'))
    else:
        graph.add_node(pydot.Node(state, shape='doublecircle'))

graph.add_edge(pydot.Edge('\2', data['start_states'][0], arrowhead='normal', color='blue'))
for edge in data['transition_function']:
    graph.add_edge(pydot.Edge(edge[0], edge[2], label=edge[1], arrowhead='normal', color='black'))

graph.write_png(sys.argv[2] if len(sys.argv)>2 else 'output.png')
