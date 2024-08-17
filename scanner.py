"""
class Scanner():
    def __int__(self, source):
        self.source = source
    def scanTokens(self):
"""


def isAtEnd(source, current):
    return current >= len(source)


def isDigit(c):
    return c >= '0' and c <= '9'


def match(c, param):
    pass


def scanTokens(source):
    """
    如果是只有+-*/和数字。输入是：2+4*3，变成下面和形式：
    NUMBER 2 2.0
    PLUS + null
    NUMBER 4 4.0
    STAR * null
    NUMBER 3 3.0
    """
    tokens = []
    start = 0
    current = 0
    while not isAtEnd(source, current):
        start = current
        c = source[current]
        if c == '+':
            tokens.append(("PLUS", c, None))
            current += 1
        elif c == '-':
            tokens.append(("MINUS", c, None))
            current += 1
        elif c == '*':
            tokens.append(("STAR", c, None))
            current += 1
        elif c == '/':
            tokens.append(("SLASH", c, None))
            current += 1
        elif c == "(":
            tokens.append(("LEFT_PAREN", c, None))
            current += 1
        elif c == ")":
            tokens.append(("RIGHT_PAREN", c, None))
            current += 1
        else:
            while isDigit(source[current]):
                current += 1
                if isAtEnd(source, current):
                    break
            text = source[start: current]
            obj = float(text)
            tokens.append(("NUMBER", text, obj))
    return tokens



