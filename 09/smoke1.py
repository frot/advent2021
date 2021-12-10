#!/usr/bin/python3

import fileinput

data = [[9] + [int(c) for c in line.strip()] + [9] for line in fileinput.input()]

b = [9] * len(data[0])
data.insert(0, b)
data.append(b)

level = 0
for row,d in enumerate(data[1:-1], 1):
    for col,p in enumerate(d[1:-1], 1):
        s = min(data[row-1][col], data[row+1][col], d[col-1], d[col+1])
        if p < s:
            level += 1+p

print(level)
