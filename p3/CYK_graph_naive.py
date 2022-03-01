import copy

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


def matrCmp(M1, M2):
    for i,row in enumerate(M1):
        for j in range(len(row)):
            if not M1[i][j] == M2[i][j]:
                return False
    return True


def CYK_graph(M, G = None, log=True):
    M1 = copy.deepcopy(M)
    for i,row in enumerate(M):
        for j in range(len(row)):
            nonterm_list = search_lhs_terminal_rule(M[i][j])
            M[i][j] = nonterm_list

    if log == True:
        logM(M, "After 1st step:")

    n = len(M)
    # динамика для 2 шага и далее:
    while not matrCmp(M1,M):
        M1 = copy.deepcopy(M)
        for k in range(n-1):
            for i in range(n):
                for j in range(n):
                    first_non_term_set = M[i][k]
                    second_non_term_set = M[k+1][j]
                    
                    for lhr in first_non_term_set:
                        for rhr in second_non_term_set:
                            ntr = search_lhs_non_terminal_rule(lhr, rhr)
                            if len(ntr) > 0:

                                try:
                                    M[i][j] += search_lhs_non_terminal_rule(lhr, rhr)
                                except TypeError:
                                    M[i][j] = search_lhs_non_terminal_rule(lhr, rhr)
                                M[i][j]=list(set(M[i][j]))

        if log:
            logM(M, prefix_msg="M after current pass:")


if __name__ == '__main__':
    graph = [
            ['a', '0', '0', '0'],
            ['0', 'd', '0', '0'],
            ['0', '0', 'd', '0'],
            ['0', '0', '0', 'c']
    ]
    CYK_graph(graph, G)

    graph2 = [
        ['a', '0', '0', '0'],
        ['0', 'd', '0', '0'],
        ['0', '0', 'd', '0'],
        ['0', '0', 'c', 'c']
    ]
    CYK_graph(graph2, G)
