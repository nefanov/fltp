%{
int cnt_vertical = 0;
int cnt_horisontal = 0;
%}

%%
aab {cnt_vertical++;}
aba {cnt_horisontal++;}
%%

int yywrap() {};

int main() {
        yylex();
        printf("\n%d %d\n", cnt_vertical, cnt_horisontal);
        return 0;
}
