# inspired by: https://github.com/tdishant/ll1-parser/blob/master/ll1_parser.py

import re
import sys

from ff_calc import get_first, get_follow

def parsing_table(productions, first, follow):
    
    print("\nParsing Table\n")

    table = {}
    for key in productions:
        for value in productions[key]:
            val = ''.join(value)
            if val != 'ε':
                for element in first[key]:
                    if(element != 'ε'):
                        if(not val[0].isupper()) :
                            if(element in val):
                                table[key, element] = val
                            else:
                                pass
                        else:
                            table[key, element] = val
            else:
                for element in follow[key]:
                    table[key, element] = val

    for key,val in table.items():
        print(key,"=>",val)

    new_table = {}
    for pair in table:
        new_table[pair[1]] = {}

    for pair in table:
        new_table[pair[1]][pair[0]] = table[pair]


    print("\n")
    print("\nParsing Table in matrix form\n")
    print(pd.DataFrame(new_table).fillna('-'))
    print("\n")
    
    return table
  
  
def main(test_gram):
    productions = {}
    grammar = open(test_gram, "r")
    
    first = {}
    follow = {}
    table = {}
    
    start = ""
    
    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)
        m = []
        for i in l:
            if (i == "" or i == None or i == '\n' or i == " " or i == "-" or i == ">"):
                pass
            else:
                m.append(i)
        
        left_prod = m.pop(0)
        right_prod = []
        t = []
        
        for j in m:
            if(j != '|'):
                t.append(j)
            else:
                right_prod.append(t)
                t = []
        
        right_prod.append(t)
        productions[left_prod] = right_prod
        
        if(start == ""):
            start = left_prod
      
    print("*****GRAMMAR*****")    
    for lhs, rhs in productions.items():
        print(lhs, ":" , rhs)
    print("")
    
    for s in productions.keys():
        first[s] = cal_first(s, productions)
    
    print("*****FIRST*****")
    for lhs, rhs in first.items():
        print(lhs, ":" , rhs)
    
    print("")
    
    for lhs in productions:
        follow[lhs] = set()
    
    for s in productions.keys():
        follow[s] = cal_follow(s, productions, first)
    
    print("*****FOLLOW*****")
    for lhs, rhs in follow.items():
        print(lhs, ":" , rhs)
    
    table = parsing_table(productions, first, follow)
    return table
    
if __name__ == '__main__':
    main(sys.argv[1]) if len(sys.argv)>1 else main("test_gram.txt")
    
  
  


