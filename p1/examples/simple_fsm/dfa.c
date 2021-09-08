#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 4096

enum states {q0 = 0, q1, q2};
enum sym {let, num, term};

// function getSym -- "toy" lexer
// performs character scope generalization (to lexem) there
// input: ascii string, position
// output: lexem
// lexem types: let -- character from a to z
//             num -- numeric character
//             term -- nul-terminator
enum sym getSym(const char* s, unsigned pos) 
{
    if (s==NULL)
        exit(1);

    char c = s[pos];

    if ('a'<=c && 'z'>=c)
        return let;
    else if('0'<=c && '9'>=c)
        return num;
    else if(c=='\0')
        return term;
    
    printf("Unacceptable character!\n");
    exit(1);
    
    return let;  
};

typedef void (*transition_callback)(enum states state, enum sym signal);

struct transition
{
    enum states new_state;
    transition_callback worker;
};

void _fxn(enum states state, enum sym signal){
    return;
};

void print_acc(enum states state, enum sym signal) {
    printf("Sequence is accepted, current state is %d\n", state);
    exit(0);
};

void print_no_acc(enum states state, enum sym signal) {
    printf("Sequence is not accepted, current state is %d\n", state);
    exit(0);
};

//This FSM(DFA) performs acceptance of programming language variable names composed only from lower ASCII english symbols and numbers
struct transition FSM_table[3][3] = {
    [q0][let] = {q1, _fxn},
    [q0][num] = {q0, print_no_acc},
    [q0][term] = {q0, print_no_acc},
    [q1][let] = {q1, _fxn},
    [q1][num] = {q1, _fxn},
    [q1][term] = {q2, print_acc}
};

void test_string(const char *s)
{
    enum states current_state = q0;
    unsigned pos = 0;
    while (1)
    {
        
        enum sym current_sym = getSym(s, pos);
        pos++;
        enum states new_state = FSM_table[current_state][current_sym].new_state;
        transition_callback worker = FSM_table[current_state][current_sym].worker;
        printf("Current = %d, sym = %d, new = %d\n", current_state, current_sym, new_state);
        if (worker != NULL)
        {
            worker(current_state, current_sym);
        }
        current_state = new_state;
    }
}

int main() 
{
    char test_buf[BUFSIZE];
    scanf("%s", test_buf);
    test_string(test_buf);
    return 0;
}

