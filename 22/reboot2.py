#!/usr/bin/python3

import re
import fileinput

mode = {'off': -1, 'on': 1}
RE = re.compile(r'(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)')

data = []
for line in fileinput.input():
    m = RE.match(line)
    cc = (mode[m[1]], (int(m[2]), int(m[3])), (int(m[4]), int(m[5])), (int(m[6]), int(m[7])))
    intersect = []
    for s, (x1, x2), (y1, y2), (z1, z2) in data:
        ix = (max(x1, cc[1][0]), min(x2, cc[1][1]))
        iy = (max(y1, cc[2][0]), min(y2, cc[2][1]))
        iz = (max(z1, cc[3][0]), min(z2, cc[3][1]))
        if ix[0] <= ix[1] and iy[0] <= iy[1] and iz[0] <= iz[1]:  # intersection
            intersect.append((-s, ix, iy, iz))
    data += intersect
    if cc[0] > 0:
        data.append(cc)

print(sum(c[0] * (1+c[1][1]-c[1][0]) * (1+c[2][1]-c[2][0]) * (1+c[3][1]-c[3][0]) for c in data))
