import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

win = {'R': 'S', 'P': 'R', 'S': 'P'}
trans = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
shape = {'R': 1, 'P': 2, 'S': 3}


@timeit
def compute(s: str) -> int:
    score = 0
    for line in s.splitlines():
        a, b = line.split()
        a = a.replace(a, trans[a])

        b = win[a] if b == 'X' else a if b == 'Y' else [k for k, v in win.items() if v == a][0]

        score += 3 if a == b else 6 if win[a] != b else 0
        score += shape[b]

    return score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 12


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
