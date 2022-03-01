G={
    'A':[['a']],
    'B':[['d']],
    'C':[['c']],
    'D':[['A','B']],
    'E':[['B','C']],
    'S':[['D','E']]
 }

def search_lhs_non_terminal_rule(first, second):
    res = []
    for k,v in G.items():
        for item in v:
            if [first,second]==item:
                res.append(k)
                print("==rule found:", first, second,"<-",k)
    return res

def search_lhs_terminal_rule(term=None):
    if not term:
        return []
    res = []
    for k,v in G.items():
        for rhs_item in v:
            if len(rhs_item) == 1:
                if term == rhs_item[0]:
                    res.append(k)
    return res


def logM(M, prefix_msg=None, postfix_msg=None):
    if prefix_msg:
        print(prefix_msg)
    for i in M:
        print(i)
    return


def logSubStr(s, substr_len, prefix_msg=None, postfix_msg=None, show_slots=False):
    if prefix_msg:
        print(prefix_msg)
    for idx in range(len(s)-substr_len+1):
        print("substring:", s[idx: idx + substr_len])
        if show_slots:
            slot = s[idx: idx + substr_len]
            print("slots:")
            for j in range(1,len(slot)):
                print(slot[:j],".",slot[j:])


def CYK(inp="", G = None, log=True):
    M = list()
    for i in range(len(inp)+1):
        M.append(['0' for i in range(len(inp)+1)])

    for i in range(len(inp)):
        M[i+1][i] = inp[i]
    if log==True:
        logM(M, "initialized matrix:")

    for i in range(len(inp)):
        nonterm_list = search_lhs_terminal_rule(M[i+1][i])
        M[i][i] = nonterm_list

    if log == True:
        logM(M, "After 1st step:")

    n = len(inp)
    # динамика для 2 шага и далее:
    for k in range(1,n):
        for j in range(k,n):
            for l in range(j-k, j):
                target_idx = (j - k, j)
                if log:
                    print("Ranges:", j-k,j,"-->", j-k,l,",",l+1,j)

                first_non_term_set = M[j-k][l]
                second_non_term_set = M[l+1][j]
                if log:
                    print("first", first_non_term_set, "second" ,second_non_term_set)
                for lhr in first_non_term_set:
                    for rhr in second_non_term_set:
                        try:
                            M[j-k][j] = list(set(M[j-k][j] + search_lhs_non_terminal_rule(lhr, rhr)))
                        except TypeError:
                            M[j - k][j] = search_lhs_non_terminal_rule(lhr, rhr)

            if log == True:
                logM(M, prefix_msg="M after: ")

        if log:
            logM(M, prefix_msg="M after: " + str(l) +" pass")

if __name__ == '__main__':
    CYK("addc", G)
    CYK("adc", G)
