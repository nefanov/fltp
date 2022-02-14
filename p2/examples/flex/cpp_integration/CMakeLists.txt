cmake_minimum_required(VERSION 3.4)
project(LexerUsage)

find_package(FLEX REQUIRED)

FLEX_TARGET(Scaner lexer.l ${Lexer_SOURCE_DIR}/lexer.cpp)

include_directories(${CMAKE_CURRENT_BINARY_DIR})

add_executable(
  LexerExample
  main.cpp
  ${FLEX_LexerUsage_OUTPUTS}
)
