%option noyywrap
%option c++
%option yyclass="Lexer"
// определения
%{
// вставка участка кода
#include <cstdio>
#include <iostream>
#include "tokens.h"
#include "lexer.hh"

%}

%%
// правила анализа
[ \t\r\n]+ {}

"up" { return TOKEN_UP; }
"down" { return TOKEN_DOWN; }
"left" { return TOKEN_LEFT; }
"right" { return TOKEN_RIGHT; }
"exit" { return TOKEN_EXIT; }

.* { std::cout << "Error " << yytext << std::endl; return TOKEN_ERROR; }
%%
