#!/usr/bin/python3

import re
import fileinput

RE = re.compile(r'(\w) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)')

data = []
def cube(m):
    for n in m[1:]:
        if not (-50 <= int(n) <= 50):
            return
    c = ((int(m[2]), int(m[4]), int(m[6])), (int(m[3]), int(m[5]), int(m[7])))
    if m[1]=='on':
        pass
    else:
        pass

for line in fileinput.input():
    cube(RE.match(line))
