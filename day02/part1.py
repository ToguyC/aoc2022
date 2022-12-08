import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

win = {1: 3, 2: 1, 3: 2}


@timeit
def compute(s: str) -> int:
    score = 0
    for line in s.splitlines():
        a, b = line.split()
        a, b = ord(a) - 64, ord(b) - 87

        score += 3 if a == b else 6 if win[a] != b else 0
        score += b

    return score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 15


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
