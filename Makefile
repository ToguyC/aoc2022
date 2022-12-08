PY:=python3
DAY_F:=$(shell printf "%02d" $(DAY))

part1:
	$(PY) main.py -d $(DAY) -p 1

part2:
	$(PY) main.py -d $(DAY) -p 2

test1:
	$(PY) -m pytest day$(DAY_F)/part1.py

test2:
	$(PY) -m pytest day$(DAY_F)/part2.py
