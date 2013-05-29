import lexer

L = lexer.Lexer()

while True:
    print L.lexString(raw_input())
