# inspired by: https://github.com/tdishant/ll1-parser/blob/master/ll1_parser.py

import re

from ff_calc import get_first, get_follow
from parsing_table import parsing_table

def analyze(string, start, table):
  accepted = True
  stack = []
  input_string = string + '$'
  stack.append('$')
  stack.append(start)
  idx = 0
  
  while len(stack) > 0: # classical algorithm
      top = stack[-1]
      print("stack:", stack, "top:", top)
      curr_string = input_string[idx] # position in the last of the string
      print(f"Current input => {curr_string}")
      if top == curr_string: # symbol on current position accepted -- go further
            stack.pop()
            idx += 1
      else: # try to search accordant rule in the parsing table
            key = (top, curr_string)
            print(f"Key in table => {key}")
            if key not in table:
                accepted = False # there is no accordant rule for this case -- string is not in L(G)
                break
            
            value = table[key] 
            if value != 'ε':
                value = value[::-1] # revert order for pushing to the stack
                value = list(value)
                
                stack.pop() # pop current non-terminal (left side of production)
                
                for element in value:
                    stack.append(element) # push right side of production
            
            else:
                stack.pop() # simply pop if 'ε'
                
      if accepted:
            print("String accepted")
      else:
            print("String not accepted")  
      
  return accepted


def preprocess(test_gram): # making parsing_table
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
        first[s] = get_first(s, productions)
    
    for lhs in productions:
        follow[lhs] = set()
    
    for s in productions.keys():
        follow[s] = get_follow(s, productions, first)
    
    table = parsing_table(productions, first, follow)
    
    grammar.close()
    return start, table
  
def parse(test_gram, string):
    start, pt = preprocess(test_gram)
    print(analyze(string, start, pt))
