import json
import sys

dfa = {}
nfa = {}
nfa_states = []
dfa_states = []

def check_input_correctness():
    if len(sys.argv) <= 2:
        print("Input is incorrect")
        sys.exit(1)
    else:
        return

    
def load_nfa():
    check_input_correctness()
    global nfa
    with open(sys.argv[1], 'r') as inpjson:
        nfa = json.loads(inpjson.read())

        
def out_dfa():
    check_input_correctness()
    global dfa
    with open(sys.argv[2], 'w') as outjson:
        outjson.write(json.dumps(dfa, indent = 4))
