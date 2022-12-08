import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def size(dirname: str, files: dict) -> int:
    MAX = 100000
    sz = 0

    for k, v in files.items():
        if k.startswith(f'{dirname}/'):
            sz += v

    return sz if sz <= MAX else 0

@timeit
def compute(s: str) -> int:
    files = {}
    dirs = {"/"}

    cwd = "/"
    for line in s.splitlines():
        if line.startswith("$ cd .."):
            cwd = os.path.dirname(cwd) or "/"
        elif line.startswith("$ cd"):
            cwd = os.path.join(cwd, line.split(' ', 2)[-1])
            dirs.add(cwd)
        elif line.startswith(('$ ls', 'dir')):
            continue
        else:
            sz, filename = line.split(' ', 1)
            files[os.path.join(cwd, filename)] = int(sz)

    return sum([size(d, files) for d in dirs])


INPUT_S = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
EXPECTED = 95437


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
