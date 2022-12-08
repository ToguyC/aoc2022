import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@timeit
def compute(s: str) -> str:
    first, rest = s.split("\n\n")
    stacks: list[list[str]] = [[]
                               for _ in range(int(first.splitlines()[-1].rstrip()[-1]))]

    for line in first.splitlines()[:-1]:
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    for stack in stacks:
        stack.reverse()

    for line in rest.splitlines():
        _, n, _, f, _, t = line.split()
        n, f, t = int(n), int(f), int(t)

        tmp = stacks[f - 1][-n:]
        del stacks[f - 1][-n:]
        stacks[t - 1].extend(tmp)

    return ''.join(s[-1] for s in stacks)


INPUT_S = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
EXPECTED = "MCD"


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: str) -> None:
    assert compute(input_s) == expected


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
