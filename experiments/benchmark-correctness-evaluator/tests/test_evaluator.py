import math
from src.solutions import naive, partially_correct, correct


def base_input():
    return [
        {"id": "a", "timestamp": 2, "value": 1, "source": "x"},
        {"id": "a", "timestamp": 2, "value": 999, "source": "x"},  # duplicate
        {"id": "b", "timestamp": 1, "value": 1.5, "source": "y"},
        {"id": " ", "timestamp": 3, "value": 2, "source": "z"},
        {"id": "c", "timestamp": -1, "value": 2, "source": "z"},
        {"id": "d", "timestamp": 4, "value": math.nan, "source": "z"},
    ]


def expected_output():
    return [
        {"id": "b", "timestamp": 1, "value": 1.5, "source": "y"},
        {"id": "a", "timestamp": 2, "value": 1, "source": "x"},
    ]


def test_naive_fails():
    assert naive.normalize_events(base_input()) != expected_output()


def test_partially_correct_fails_numeric_integrity():
    out = partially_correct.normalize_events(base_input())
    assert out[0]["value"] == 1.5
    assert isinstance(out[0]["value"], float)
    assert out != expected_output()


def test_correct_passes():
    assert correct.normalize_events(base_input()) == expected_output()
