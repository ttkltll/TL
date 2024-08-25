from astPrinter import Literal, Binary, Unary, Grouping, PrintStatement, DeclareStatement, AssignStatement
from environment import bind_dict
from tokenType import TokenType

current = 0

def parse(tokens):
    global current
    current = 0
    expr = statement(tokens)
    return expr


def statement(tokens):
    if match(tokens[current], TokenType.PRINT):
        expr = expression(tokens[1:])
        expr = PrintStatement(expr)
    elif match(tokens[current], TokenType.VAR):
        expr = DeclareStatement(tokens[1:][0])
    elif match(tokens[current], TokenType.IDENTIFIER):
        name = tokens[0].lexeme
        expr = expression(tokens[2:])
        expr = AssignStatement(name, expr)

    return expr


def expression(tokens):
    return term(tokens)


def term(tokens):
    global current
    expr = factor(tokens)
    while current < len(tokens) and match(tokens[current], TokenType.MINUS, TokenType.PLUS):
        current += 1
        operator = tokens[current-1]
        right = factor(tokens)
        expr = Binary(expr, operator, right)
    return expr


def factor(tokens):
    global current
    expr = unary(tokens)
    while current < len(tokens) and match(tokens[current], TokenType.STAR, TokenType.SLASH):
        current += 1
        operator = tokens[current-1]
        right = unary(tokens)
        expr = Binary(expr, operator, right)
    return expr


def unary(tokens):
    global current
    if current < len(tokens) and match(tokens[current], TokenType.BANG, TokenType.MINUS):
        current += 1
        operator = tokens[current-1]
        right = unary(tokens)
        return Unary(operator, right)
    return primary(tokens)


def primary(tokens):
    global current
    token = tokens[current]
    if current < len(tokens) and match(token, TokenType.NUMBER, TokenType.STRING):
        current += 1
        return Literal(token.literal)
    if current < len(tokens) and match(token, TokenType.TRUE):
        current += 1
        return Literal(True)
    if current < len(tokens) and match(token, TokenType.FALSE):
        current += 1
        return Literal(False)
    if current < len(tokens) and match(token, TokenType.NIL):
        current += 1
        return Literal(None)
    if current < len(tokens) and match(token, TokenType.IDENTIFIER):
        current += 1
        value = bind_dict[token.lexeme]
        return Literal(value)
    if current < len(tokens) and match(token, TokenType.LEFT_PAREN):
        current += 1
        expr = expression(tokens)
        token = tokens[current]
        if current < len(tokens) and match(token, TokenType.RIGHT_PAREN):
            current += 1
        return Grouping(expr)


def match(token, *types):
    for type in types:
        if token.type == type:
            return True
    return False
