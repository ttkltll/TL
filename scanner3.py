from myToken import Token
from tokenType import TokenType

def isAtEnd(source, current):
    return current >= len(source)

def isDigit(c):
    return c >= '0' and c <= '9'

def isAlpha(c):
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

def isAlphaNumeric(c):
    return isAlpha(c) or isDigit(c)

def addToken(type, text, tokens, current, line, literal=None):
    tokens.append(Token(type, text, literal, line))
    return tokens, current + 1, line

def match(source, current, expected):
    if isAtEnd(source, current) or source[current] != expected:
        return False
    return True

def scanTokens(source):
    tokens = []
    start = 0
    current = 0
    line = 1
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

    def advance():
        nonlocal current
        current += 1
        return source[current - 1]

    def peek():
        return '\0' if isAtEnd(source, current) else source[current]

    def peekNext():
        return '\0' if current + 1 >= len(source) else source[current + 1]

    def scanString():
        nonlocal current, line
        while peek() != '"' and not isAtEnd(source, current):
            if peek() == '\n':
                line += 1
            advance()

        if isAtEnd(source, current):
            print("Unterminated string.")
            return

        advance()
        value = source[start + 1:current - 1]
        tokens.append(Token(TokenType.STRING, value, value, line))

    def scanNumber():
        nonlocal current
        while isDigit(peek()):
            advance()

        if peek() == '.' and isDigit(peekNext()):
            advance()
            while isDigit(peek()):
                advance()

        text = source[start:current]
        tokens.append(Token(TokenType.NUMBER, text, float(text), line))

    def scanIdentifier():
        nonlocal current
        while isAlphaNumeric(peek()):
            advance()

        text = source[start:current]
        token_type = keywords.get(text, TokenType.IDENTIFIER)
        tokens.append(Token(token_type, text, None, line))

    while not isAtEnd(source, current):
        start = current
        c = advance()

        if c == '(':
            tokens, current, line = addToken(TokenType.LEFT_PAREN, c, tokens, current, line)
        elif c == ')':
            tokens, current, line = addToken(TokenType.RIGHT_PAREN, c, tokens, current, line)
        elif c == '{':
            tokens, current, line = addToken(TokenType.LEFT_BRACE, c, tokens, current, line)
        elif c == '}':
            tokens, current, line = addToken(TokenType.RIGHT_BRACE, c, tokens, current, line)
        elif c == ',':
            tokens, current, line = addToken(TokenType.COMMA, c, tokens, current, line)
        elif c == '.':
            tokens, current, line = addToken(TokenType.DOT, c, tokens, current, line)
        elif c == '-':
            tokens, current, line = addToken(TokenType.MINUS, c, tokens, current, line)
        elif c == '+':
            tokens, current, line = addToken(TokenType.PLUS, c, tokens, current, line)
        elif c == ';':
            tokens, current, line = addToken(TokenType.SEMICOLON, c, tokens, current, line)
        elif c == '*':
            tokens, current, line = addToken(TokenType.STAR, c, tokens, current, line)
        elif c == '!':
            token_type = TokenType.BANG_EQUAL if match(source, current, '=') else TokenType.BANG
            tokens, current, line = addToken(token_type, c, tokens, current, line)
            current += 1 if token_type == TokenType.BANG_EQUAL else 0
        elif c == '=':
            token_type = TokenType.EQUAL_EQUAL if match(source, current, '=') else TokenType.EQUAL
            tokens, current, line = addToken(token_type, c, tokens, current, line)
            current += 1 if token_type == TokenType.EQUAL_EQUAL else 0
        elif c == '<':
            token_type = TokenType.LESS_EQUAL if match(source, current, '=') else TokenType.LESS
            tokens, current, line = addToken(token_type, c, tokens, current, line)
            current += 1 if token_type == TokenType.LESS_EQUAL else 0
        elif c == '>':
            token_type = TokenType.GREATER_EQUAL if match(source, current, '=') else TokenType.GREATER
            tokens, current, line = addToken(token_type, c, tokens, current, line)
            current += 1 if token_type == TokenType.GREATER_EQUAL else 0
        elif c == '/':
            if match(source, current, '/'):
                while peek() != '\n' and not isAtEnd(source, current):
                    advance()
            else:
                tokens, current, line = addToken(TokenType.SLASH, c, tokens, current, line)
        elif c in {' ', '\r', '\t'}:
            pass
        elif c == '\n':
            line += 1
        elif c == '"':
            scanString()
        elif isDigit(c):
            scanNumber()
        elif isAlpha(c):
            scanIdentifier()
        else:
            print(f"Unexpected character: {c}")

    tokens.append(Token(TokenType.EOF, "", None, line))
    return tokens
