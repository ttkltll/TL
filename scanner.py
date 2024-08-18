from myToken import Token
from tokenType import TokenType


def isAtEnd(source, current):
    return current >= len(source)


def isDigit(c):
    return c >= '0' and c <= '9'


def addToken(token_type: TokenType, c: str, tokens: list[Token], current: int, line: int):
    tokens.append(Token(token_type, c, None, line))
    current += 1
    return tokens, current, line


def scanTokens(source):
    tokens = []
    start = 0
    current = 0
    keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE,
    }

    while not isAtEnd(source, current):
        start = current
        c = source[current]
        line = 1
        if c == '+':
            tokens, current, line = addToken(TokenType.PLUS, c, tokens, current, line)
        elif c == '-':
            tokens, current, line = addToken(TokenType.MINUS, c, tokens, current, line)
        elif c == '*':
            tokens, current, line = addToken(TokenType.STAR, c, tokens, current, line)
        elif c == '/':
            tokens, current, line = addToken(TokenType.SLASH, c, tokens, current, line)
        elif c == '{':
            tokens, current, line = addToken(TokenType.LEFT_BRACE, c, tokens, current, line)
        elif c == '}':
            tokens, current, line = addToken(TokenType.RIGHT_BRACE, c, tokens, current, line)
        elif c == '(':
            tokens, current, line = addToken(TokenType.LEFT_PAREN, c, tokens, current, line)
        elif c == ')':
            tokens, current, line = addToken(TokenType.RIGHT_PAREN, c, tokens, current, line)
        elif c == ',':
            tokens, current, line = addToken(TokenType.COMMA, c, tokens, current, line)
        elif c == '.':
            tokens, current, line = addToken(TokenType.DOT, c, tokens, current, line)
        elif c == ';':
            tokens, current, line = addToken(TokenType.SEMICOLON, c, tokens, current, line)
        elif isDigit(c):
            while isDigit(source[current]):
                current += 1
                if isAtEnd(source, current):
                    break
            text = source[start: current]
            obj = float(text)
            tokens.append(Token("NUMBER", text, obj, line))

    return tokens
