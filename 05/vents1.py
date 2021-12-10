#!/usr/bin/python3

import fileinput
from functools import reduce
from pprint import pprint

DIM = 1000
m = [[0 for x in range(DIM)] for y in range(DIM)]

for line in fileinput.input():
    s,_,e = line.split()
    sx,sy = [int(i) for i in s.split(',')]
    ex,ey = [int(i) for i in e.split(',')]
    if (sx != ex) and (sy != ey):
        continue
    if sx > ex:
        sx,ex = ex,sx
    if sy > ey:
        sy,ey = ey,sy
    #print(sx,sy,ex,ey)
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            m[x][y] += 1

#pprint(m)

count = reduce(lambda s,n: s+1 if n>1 else s, [col for row in m for col in row], 0)
print(count)
