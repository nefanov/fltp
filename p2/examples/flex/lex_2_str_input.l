/* Declaring two counters one for number 
of lines other for number of characters */
%{
int no_of_lines = 0;
int no_of_chars = 0;
%}
  
/***rule 1 counts the number of lines, 
rule 2 counts the number of characters 
and rule 3 specifies when to stop 
taking input***/
%%
\n      ++no_of_lines;
.       ++no_of_chars;
end     return 0;
%%
  
/*** User code section***/
int yywrap(){}

int main() {
    yy_scan_buffer("a test string \n end");
    yylex();
    printf("%d %d\n", no_of_lines, no_of_chars);
    return 0;
}
