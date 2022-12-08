import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@timeit
def compute(s: str) -> int:
    elves: list[list[int]] = []

    current_elf = 0
    lines = s.splitlines()

    for _ in range(lines.count("") + 1):
        elves.append([])

    for line in lines:
        if line == "":
            current_elf += 1
            continue
    
        elves[current_elf].append(int(line))

    return max([sum(elf) for elf in elves])


INPUT_S = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
EXPECTED = 24000


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
