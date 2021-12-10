#!/usr/bin/python3

import fileinput

data = [int(line) for line in fileinput.input()]

print(len([x for x, y in zip(data, data[1:]) if x < y]))

