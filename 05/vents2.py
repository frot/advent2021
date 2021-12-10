#!/usr/bin/python3

import fileinput
from functools import reduce

DIM = 1000
m = [[0 for x in range(DIM)] for y in range(DIM)]

def pgrid():
    for y in range(DIM):
        for x in range(DIM):
            print(m[x][y], end=' ')
        print()
    print()

for line in fileinput.input():
    s,_,e = line.split()
    sx,sy = [int(i) for i in s.split(',')]
    ex,ey = [int(i) for i in e.split(',')]
    if not ((sx == ex) or (sy == ey) or (abs(ex-sx) == abs(ey-sy))):
        continue
    if sx < ex:
        rx = range(sx, ex+1, 1)
    elif ex < sx:
        rx = range(sx, ex-1, -1)
    else:
        rx = [sx] * DIM
    if sy < ey:
        ry = range(sy, ey+1, 1)
    elif ey < sy:
        ry = range(sy, ey-1, -1)
    else:
        ry = [sy] * DIM
    print(sx,sy,ex,ey)
    for x,y in zip(rx, ry):
        m[x][y] += 1

#pgrid()
count = reduce(lambda s,n: s+1 if n>1 else s, [col for row in m for col in row], 0)
print(count)
