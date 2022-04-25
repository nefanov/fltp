# Note: if grammar has eps-rules, add loops on ititialization phase (TO DO)

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
            if [first,second] == item:
                res.append(k)
                #print("==rule found:", first, second,"<-",k)
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


def hellings(M, G=None, log=True):
    print("==========Hellings algorithm===========")
    r = []
    m = []

    for i, row in enumerate(M):
        for j in range(len(row)):
            nonterm_list = search_lhs_terminal_rule(M[i][j])
            if len(nonterm_list) > 0:
                for N in nonterm_list:
                    r.append((N,i,j))
    m += r

    while len(m) > 0:
        entry = m[0]
        m = m[1:]
        for r_item in r:
            if r_item[2] == entry[1]:
                ntr = search_lhs_non_terminal_rule(entry[0], r_item[0]) # try to concat right
                if len(ntr) > 0:
                    for n in ntr:
                        m.append((n, r_item[1], entry[1]))
                        r.append((n, r_item[1], entry[1]))
        for r_item in r:
            if r_item[2] == entry[1]:
                ntr = search_lhs_non_terminal_rule(r_item[0], entry[0]) # try to concat left
                if len(ntr) > 0:
                    for n in ntr:
                        m.append((n, entry[2], r_item[1]))
                        r.append((n, entry[2], r_item[1]))
    return r


if __name__ == '__main__':
    print("==========Test 1===========")

    graph1 = [
        ['0', 'a', '0', '0', '0'],
        ['0', '0', 'd', '0', '0'],
        ['0', '0', '0', 'd', '0'],
        ['0', '0', '0', '0', 'c'],
        ['0', '0', '0', '0', '0'],
    ]

    print(hellings(graph1, G))

    print("==========Test 2===========")
    graph2 = [
        ['0', 'a', '0', '0', '0'],
        ['0', '0', 'd', '0', '0'],
        ['0', '0', '0', 'd', '0'],
        ['0', '0', '0', 'c', 'c'],
        ['0', '0', '0', '0', '0']
    ]
    print(hellings(graph2,G))
