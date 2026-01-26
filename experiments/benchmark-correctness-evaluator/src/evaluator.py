import traceback
from typing import Callable, List, Dict, Any

Event = Dict[str, Any]


class EvaluationResult:
    def __init__(self, passed: bool, error: str | None = None):
        self.passed = passed
        self.error = error


def evaluate(
    fn: Callable[[List[Any]], List[Event]],
    test_cases: List[List[Any]],
    expected: List[List[Event]],
) -> EvaluationResult:
    try:
        for inp, exp in zip(test_cases, expected):
            out = fn(inp)
            if out != exp:
                return EvaluationResult(
                    False,
                    f"Mismatch.\nExpected: {exp}\nGot: {out}",
                )
        return EvaluationResult(True)
    except Exception:
        return EvaluationResult(False, traceback.format_exc())
