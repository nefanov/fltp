import json
import sys
import os

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

def load_dfa():
    return load_fa()

def load_nfa():
    return load_fa()

def load_fa():
    check_input_correctness()
    global nfa
    with open(sys.argv[1], 'r') as inpjson:
        nfa = json.loads(inpjson.read())
        return nfa

        
def out_dfa(fa):
    out_fa(fa)

def out_fa(fa):
    check_input_correctness()
    with open(sys.argv[2], 'w') as outjson:
        outjson.write(json.dumps(fa, indent = 4))

if __name__ == '__main__':
    raw=open(os.getcwd() + os.sep + sys.argv[1]).read()
    print(json.loads(raw))
