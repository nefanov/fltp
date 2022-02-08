import faio

def get_power_set(nfa_states):
    powerset = [[]]
    for i in nfa_states:
        for subset in powerset:
            powerset = powerset + [list(subset) + [i]]
    return powerset
  
  
if __name__ == "__main__":
    nfa = faio.load_nfa()
    dfa = {}
    dfa['states'] = []
    dfa['letters'] = nfa['letters'] # \Sigma are equal
    dfa['transition_function'] = []
    
    nfa_states = []
    for state in nfa['states']:
        nfa_states.append(state) # Q_0 DFA == Q NFA

    dfa_states = get_power_set(nfa_states)[1:] # set of sets of the states

    dfa['states'] = []
    for states in dfa_states:
        dfa['states'].append(states[:])
        for letter in nfa['letters']:
            q_to = []
            for state in states:
                for val in nfa['transition_function']:
                    src = val[0]
                    inp = val[1]
                    dst = val[2]
                    if state == src and letter == inp:
                        if dst not in q_to:
                            q_to.append(dst)
            q_states = []
            for i in states:
                q_states.append(i)
            dfa['transition_function'].append([sorted(q_states), letter, sorted(q_to)])
    dfa['start_states'] = []
    for state in nfa['start_states']:
        dfa['start_states'].append([state])
    dfa['final_states'] = []
    for states in dfa['states']:
        for state in states:
            if state in nfa['final_states'] and states not in dfa['final_states']:
                dfa['final_states'].append(states)
    
    # finalize labels as strings:
    for i, item in enumerate(dfa['states']):
        dfa['states'][i] = "_".join(item)

    for i, item in enumerate(dfa['start_states']):
        dfa['start_states'][i] = "_".join(item)

    for i, item in enumerate(dfa['final_states']):
        dfa['final_states'][i] = "_".join(item)
    
    for i, item in enumerate(dfa['transition_function']):
        dfa['transition_function'][i][0] = "_".join(item[0])
        dfa['transition_function'][i][2] = "_".join(item[2])
    faio.out_dfa(dfa)
    
