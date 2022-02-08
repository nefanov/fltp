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

def out_fa(fa, need_finalize_for_plot=True):
    check_input_correctness()
    with open(sys.argv[2], 'w') as outjson:
        if need_finalize_for_plot:
        # finalize labels as strings:
            for i, item in enumerate(fa['states']):
                fa['states'][i] = "_".join(item)

            for i, item in enumerate(fa['start_states']):
                fa['start_states'][i] = "_".join(item)

            for i, item in enumerate(fa['final_states']):
                fa['final_states'][i] = "_".join(item)

            for i, item in enumerate(fa['transition_function']):
                fa['transition_function'][i][0] = "_".join(item[0])
                fa['transition_function'][i][2] = "_".join(item[2])
        
        outjson.write(json.dumps(fa, indent = 4))

if __name__ == '__main__':
    raw=open(os.getcwd() + os.sep + sys.argv[1]).read()
    print(json.loads(raw))
