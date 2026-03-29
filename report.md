# Propositional Logic Evaluator Report

## The Grammar Of The Language

The evaluator accepts propositional-logic expressions built from truth values,
logical operators, and parentheses.

Accepted truth values:

- `T` / `t`
- `F` / `f`

Accepted operators:

- `AND` / `and` / `A`
- `OR` / `or` / `V`
- `NOT` / `not`

Parentheses `(` and `)` are used for grouping.

The grammar used by the parser is:

```ebnf
statement    ::= expr
expr         ::= expr OR term | term
term         ::= term AND factor | factor
factor       ::= NOT factor
               | TRUE
               | FALSE
               | "(" expr ")"
```

This grammar gives the following precedence:

1. Parentheses
2. `NOT`
3. `AND`
4. `OR`

For example, the expression:

```txt
T OR F AND T
```

is parsed as:

```txt
T OR (F AND T)
```

## Type Of The Parser

The implementation uses `sly.Parser`, which is a bottom-up parser generator for
Python. In practice, this is an LALR-style parser.

The parser is implemented in:

```txt
src/example/components/parsers.py
```

Operator precedence is encoded with the parser's `precedence` setting so that:

- `OR` has lower precedence than `AND`
- `NOT` has higher precedence than both `AND` and `OR`

## Method Of Translation And Integration Of Parser And Translation

The system uses AST-based translation instead of immediate evaluation.

### 1. Lexical Analysis

The lexer in:

```txt
src/example/components/lexica.py
```

reads the input string and converts it into tokens such as:

- `TRUE`
- `FALSE`
- `AND`
- `OR`
- `NOT`
- `LPAREN`
- `RPAREN`

### 2. Parsing

The parser in:

```txt
src/example/components/parsers.py
```

does not compute the final answer immediately. Instead, it builds an Abstract
Syntax Tree (AST).

For example:

```txt
T OR F AND T
```

is translated into a tree whose root is `OR`, with:

- left child: `T`
- right child: `AND(F, T)`

### 3. AST Representation

The AST node classes are defined in:

```txt
src/example/components/ast/statement.py
```

The main node types are:

- `ExpressionLiteral` for truth values
- `ExpressionUnary` for `NOT`
- `ExpressionBinary` for `AND` and `OR`

### 4. Evaluation And Prefix Translation

After parsing is complete, the root AST node is evaluated. The `evaluate()`
method recursively evaluates child nodes and returns both:

- the final truth value
- the equivalent expression in prefix notation

For example:

```txt
Input:   T OR F AND T
Result:  T
Prefix:  OR T AND F T
```

### 5. Integration In The Application

The GUI in:

```txt
src/example/main.py
```

connects the parser and translation stages as follows:

1. Read the user input
2. Tokenize the input with the lexer
3. Parse the tokens into an AST
4. Evaluate the AST
5. Display:
   - the truth value
   - the prefix notation

This separation between lexer, parser, AST, and evaluation makes the program
easier to understand, test, and extend.
