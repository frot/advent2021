#!/usr/bin/python3

import re
import fileinput

mode = {'off': 0, 'on': 1}
RE = re.compile(r'(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)')

data = []
xmin, xmax = 50, -50
ymin, ymax = 50, -50
zmin, zmax = 50, -50

for line in fileinput.input():
    m = RE.match(line)
    cc = (mode[m[1]], (int(m[2]), int(m[3])), (int(m[4]), int(m[5])), (int(m[6]), int(m[7])))
    if all(c[0] <= 50 and c[1] >= -50 for c in cc[1:]):
        data.append(cc)
        xmin = min(xmin, cc[1][0])
        xmax = max(xmax, cc[1][1])
        ymin = min(ymin, cc[2][0])
        ymax = max(ymax, cc[2][1])
        zmin = min(zmin, cc[3][0])
        zmax = max(zmax, cc[3][1])

data.reverse()
count = 0
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        for z in range(zmin, zmax+1):
            for m, (x1, x2), (y1, y2), (z1, z2) in data:
                if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
                    count += m
                    break

print(count)
