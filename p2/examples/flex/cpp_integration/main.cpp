//main.cpp

#include <iostream>
#include "lexer.hh"


int main() {
  Lexer lexer;
  while (1) {
    int token = lexer.ScanToken();
    std::cout << token << std::endl;
  }
  return 0; 
}
