import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@timeit
def compute(s: str) -> int:
    score = 0

    for line in s.splitlines():
        half = len(line) // 2
        l, r = line[:half], line[half:]

        item = ''.join(set(l).intersection(r))
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
EXPECTED = 157


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
