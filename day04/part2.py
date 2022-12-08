import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@timeit
def compute(s: str) -> int:
    union = 0

    for line in s.splitlines():
        g0, g1 = line.split(',')
        s0, e0 = g0.split('-')
        s1, e1 = g1.split('-')
        s0, e0, s1, e1 = int(s0), int(e0), int(s1), int(e1)

        if s0 <= s1 <= e0 or s1 <= s0 <= e1:
            union += 1

    return union


INPUT_S = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
EXPECTED = 4


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
