from sly import Parser

from .ast.statement import (
    EvaluationResult,
    Expression,
    ExpressionBinary,
    ExpressionLiteral,
    ExpressionUnary,
    Operations,
)
from .lexica import MyLexer


class ASTParser(Parser):
    debugfile = "parser.out"
    start = "statement"
    tokens = MyLexer.tokens
    precedence = (
        ("left", OR),
        ("left", AND),
        ("right", NOT),
    )

    @_('expr')
    def statement(self, p) -> Expression:
        return p.expr

    @_('expr OR term')
    def expr(self, p) -> Expression:
        return ExpressionBinary(Operations.OR, p.expr, p.term)

    @_('term')
    def expr(self, p) -> Expression:
        return p.term

    @_('term AND factor')
    def term(self, p) -> Expression:
        return ExpressionBinary(Operations.AND, p.term, p.factor)

    @_('factor')
    def term(self, p) -> Expression:
        return p.factor

    @_('NOT factor')
    def factor(self, p) -> Expression:
        return ExpressionUnary(Operations.NOT, p.factor)

    @_('TRUE')
    def factor(self, p) -> Expression:
        return ExpressionLiteral(True)

    @_('FALSE')
    def factor(self, p) -> Expression:
        return ExpressionLiteral(False)

    @_('LPAREN expr RPAREN')
    def factor(self, p) -> Expression:
        return p.expr


MyParser = ASTParser


if __name__ == "__main__":
    lexer = MyLexer()
    parser = ASTParser()
    text = "T OR F AND NOT ( T OR F )"
    tree = parser.parse(lexer.tokenize(text))
    result: EvaluationResult = tree.evaluate()
    print("truth_value:", result.display_value())
    print("prefix:", result.prefix)
