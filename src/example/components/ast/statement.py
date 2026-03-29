from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Operations(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"


@dataclass
class EvaluationResult:
    truth_value: bool
    prefix: str

    def display_value(self) -> str:
        return "T" if self.truth_value else "F"


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> EvaluationResult:
        raise NotImplementedError


@dataclass
class ExpressionLiteral(Expression):
    value: bool

    def evaluate(self) -> EvaluationResult:
        prefix = "T" if self.value else "F"
        return EvaluationResult(truth_value=self.value, prefix=prefix)


@dataclass
class ExpressionUnary(Expression):
    operation: Operations
    operand: Expression

    def evaluate(self) -> EvaluationResult:
        operand_result = self.operand.evaluate()

        if self.operation != Operations.NOT:
            raise ValueError(f"Unsupported unary operation: {self.operation}")

        return EvaluationResult(
            truth_value=not operand_result.truth_value,
            prefix=f"NOT {operand_result.prefix}",
        )


@dataclass
class ExpressionBinary(Expression):
    operation: Operations
    left: Expression
    right: Expression

    def evaluate(self) -> EvaluationResult:
        left_result = self.left.evaluate()
        right_result = self.right.evaluate()

        if self.operation == Operations.AND:
            truth_value = left_result.truth_value and right_result.truth_value
        elif self.operation == Operations.OR:
            truth_value = left_result.truth_value or right_result.truth_value
        else:
            raise ValueError(f"Unsupported binary operation: {self.operation}")

        return EvaluationResult(
            truth_value=truth_value,
            prefix=f"{self.operation.value} {left_result.prefix} {right_result.prefix}",
        )
