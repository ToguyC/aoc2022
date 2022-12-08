# aoc2022
https://adventofcode.com/2022

# usage
Duplicate the folder `day00` for the day you are working on.<br>
Download the input file as `input.txt` in the folder you just duplicated.<br>
Code your things in the `compute` method.<br>
Run your code using `make part<1-2> DAY="<0-25 | 00-25>"`.<br>
If you want to test `make test<1-2> DAY="<0-25 | 00-25>"`.<br>

# about

For 2022, I'm planing to implement in python

# timing
* comparing to these numbers isn't necessarily useful
* normalize your timing to day 1 part 1 and compare
* these timings are very non-scientific

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | grep -o "..$" | xargs --replace bash -xc 'make part1 DAY="{}"; make part2 DAY="{}"'                                                   130 ↵
+ make part1 DAY=01
python3 main.py -d 01 -p 1
> 0.0004
73211
+ make part2 DAY=01
python3 main.py -d 01 -p 2
> 0.0004
213958
```
