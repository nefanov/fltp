//main.cpp

#include <iostream>
#include "lexer.hh"

#include "tokens.h"


int main() {
  Lexer lexer;
  while (1) {
    int token = lexer.ScanToken();
    std::cout << token << std::endl;
    if (token == TOKEN_EXIT)
      return 0;
  }
  return 0; 
}
