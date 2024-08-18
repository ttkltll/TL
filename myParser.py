from astPrinter import Literal, Binary, Unary, Grouping

current = 0

def parse(tokens):
    global current
    current = 0
    statements = []
    statements.append(expression(tokens))
    return statements


def expression(tokens):
    return term(tokens)


def term(tokens):
    global current
    expr = factor(tokens)
    while current < len(tokens) and match(tokens[current], 'MINUS', "PLUS"):
        current += 1
        operator = tokens[current-1][1]
        right = factor(tokens)
        expr = Binary(expr, operator, right)
    return expr


def factor(tokens):
    global current
    expr = unary(tokens)
    while current < len(tokens) and match(tokens[current], "STAR", "SLASH"):
        current += 1
        operator = tokens[current-1][1]
        right = unary(tokens)
        expr = Binary(expr, operator, right)
    return expr


def unary(tokens):
    global current
    if current < len(tokens) and match(tokens[current], "BANG", "MINUS"):
        current += 1
        operator = tokens[current-1][1]
        right = unary(tokens)
        return Unary(operator, right)
    return primary(tokens)


def primary(tokens):
    global current
    token = tokens[current]
    if current < len(tokens) and match(token, "NUMBER"):
        current += 1
        return Literal(token[2])
    if current < len(tokens) and match(token, "LEFT_PAREN"):
        current += 1
        expr = expression(tokens)
        token = tokens[current]
        if current < len(tokens) and match(token, "RIGHT_PAREN"):
            current += 1
        return Grouping(expr)


def match(token, *types):
    for type in types:
        if token[0] == type:
            return True
    return False
