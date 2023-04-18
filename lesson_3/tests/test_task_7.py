from lesson_3.task_7 import fib
import pytest


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ]
)
def test_fib(index, expected):
    assert fib(index) == expected
