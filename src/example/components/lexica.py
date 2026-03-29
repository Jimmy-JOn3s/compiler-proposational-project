from sly import Lexer
import sly


class MyLexer(Lexer):
    """
    Tokenizer for the propositional logic language used in the assignment.
    Supported input forms:
    - Truth values: T, F
    - Operators: AND / A, OR / V, NOT
    - Parentheses: (, )
    """

    tokens = {TRUE, FALSE, AND, OR, NOT, LPAREN, RPAREN}

    ignore = " \t"

    # Support both the assignment's symbolic spelling and readable words.
    TRUE = r"T|t"
    FALSE = r"F|f"
    AND = r"AND|and|A"
    OR = r"OR|or|V"
    NOT = r"NOT|not"
    LPAREN = r"\("
    RPAREN = r"\)"

    @_(r"\n+")
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self, t):
        self.index += 1
        print(f"ERROR: Illegal character '{t.value[0]}' at line {self.lineno}")


if __name__ == "__main__":
    string_input: str = "T OR F AND NOT ( T OR F )"
    lex: Lexer = MyLexer()
    token: sly.lex.Token
    for token in lex.tokenize(string_input):
        print(token)
