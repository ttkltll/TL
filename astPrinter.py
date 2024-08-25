"""
### 实现下面：
（2+5）*9+4
(+（* （+ 2 5） 9) 4)
（2+5）*-9+4
(+（* （+ 2 5） 9) 4)
2+5+4*6
2+5*7


### 树的构造方法不是线性遍历tokens，而是用
Binary((Literal(2)  + Binary(Literal(5), * , Literal(7))))

上面如何打印出 （+（* 5 7）2)
"""
from environment import bind_dict
from interpreter import evaluate
from tokenType import TokenType


class Binary():
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"({self.operator} {self.left} {self.right})"
    def evaluate(self):
        left = evaluate(self.left)
        right = evaluate(self.right)
        if self.operator.type == TokenType.PLUS:
            if isinstance(left, float) and isinstance(right, float):
                return float(left) + float(right)
            elif isinstance(left, str) and isinstance(right, str):
                return str(left) + str(right)
        elif self.operator.type == TokenType.MINUS:
            return float(left) - float(right)
        elif self.operator.type == TokenType.STAR:
            return float(left) * float(right)
        elif self.operator.type == TokenType.SLASH:
            return float(left) / float(right)


class Grouping():
    def __init__(self, expression):
        self.expression = expression
    def __repr__(self):
        return f"(group {self.expression})"
    def evaluate(self):
        value = evaluate(self.expression)
        return value


class Literal():
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
    def evaluate(self):
        return self.value


class Unary():
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"({self.operator} {self.right})"

### 以下是定义语句
class PrintStatement():
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self):
        value = evaluate(self.expression)
        print(value)


class DeclareStatement():
    def __init__(self, name):
        self.name = name.lexeme
    def evaluate(self):
        bind_dict[self.name] = None


class AssignStatement():
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
    def evaluate(self):
        value = evaluate(self.expression)
        bind_dict[self.name] = value




if __name__ == "__main__":
    """
    2+5*7
    2*(4+2)打印出：（* 2 (+ 4 2))
    """
    expression = Binary(Literal(2), '+', Binary(Literal(5), '*', Literal(7)))
    expression2 = Binary(Literal(2), '*', Grouping(Binary(Literal(4), '+', Literal(2))))
    print(expression)
    print(expression2)

