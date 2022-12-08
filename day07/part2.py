import os
import pytest
from .support import timeit


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def size(dirname: str, files: dict) -> int:
    sz = 0
    
    for k, v in files.items():
        if k.startswith(f'{dirname}/'):
            sz += v

    return sz

@timeit
def compute(s: str) -> int:
    files = {}
    dirs = {"/"}

    FILESYSTEM: int = 70000000
    MIN_SPACE: int = 30000000

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
 
    root = sum(files.values())
    sizes = [root] + [size(d, files) for d in dirs]

    need_to_delete = MIN_SPACE - (FILESYSTEM - root)
    sizes = [s for s in sizes if s >= need_to_delete]

    return min(sizes)


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
EXPECTED = 24933642


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
