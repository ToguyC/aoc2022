import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@timeit
def compute(s: str) -> int:
    score = 0

    lines = iter(s.splitlines())
    for l0, l1, l2 in zip(lines, lines, lines):
        item = ''.join(set(l0).intersection(l1).intersection(l2))
        priority = ord(item) - 96 if item.islower() else ord(item) - 64 + 26
        score += priority

    return score


INPUT_S = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
EXPECTED = 70


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
