#!/usr/bin/python3

import fileinput

data = [int(line) for line in fileinput.input()]

grp = [sum(x) for x in zip(data, data[1:], data[2:])]

print(len([x for x, y in zip(grp, grp[1:]) if x < y]))
