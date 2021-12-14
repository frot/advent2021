#!/usr/bin/python3

import fileinput
from collections import defaultdict

def pprint(s):
    for row in s:
        print(''.join(row))

points = []
folds = []

for line in fileinput.input():
    line = line.strip()
    if ',' in line:
        x,y=line.split(',')
        points.append([int(x), int(y)])
    elif '=' in line:
        d,n=line.split('=')
        folds.append((0 if d[-1]=='x' else 1, int(n)))

for d,n in folds[:1]:
    for p in points:
        if p[d] > n:
            p[d] = 2*n - p[d]

xmax = 1+max([x for x,_ in points])
ymax = 1+max([y for _,y in points])
print(xmax, ymax)

sheet = [['.' for x in range(xmax)] for y in range(ymax)]
count = 0
for x,y in points:
    if sheet[y][x] != '#':
        sheet[y][x] = '#'
        count += 1

#pprint(sheet)
print(count)
