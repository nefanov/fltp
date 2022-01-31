def recognize(string, machine, acceptStates):
        index = 0 # Beginning of tape
        currentState = 0 # Initial state of machine
        while True:
                if index == len(string):
                        if currentState in acceptStates:
                                return True
                        else:
                                return False
                elif string[index] in machine[currentState].keys():
                        prevState = currentState
                        currentState = machine[currentState][string[index]]
                        print("Transition to state:", currentState,"from state", prevState, "by reading", string[index])
                        index+=1
                else:
                        return False

stateTranTable = {0:{"l":1}, 1:{"n":1,"!":2}, 2:{}}
print(recognize("l!",stateTranTable, [2]))
