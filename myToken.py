class Token:
    def __init__(self, token_type, lexeme, literal, line):
        self.type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"<Token> {self.type} {self.lexeme} {self.literal}"

    def __repr__(self):
        return self.__str__()
