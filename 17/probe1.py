#!/usr/bin/python3

import re
import fileinput

def shoot(x1, x2, y1, y2):
    print(x1, x2, y1, y2)
    dy = -y1-1
    print(dy)
    ymax = dy*(dy + 1)/2
    print(ymax)
    

for line in fileinput.input():
    m = re.search(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line)
    shoot(int(m[1]), int(m[2]), int(m[3]), int(m[4]))


"""
d = dy - n

d = dy - 2*dy - 1

d = -dy - 1

-d-1 = dy

ymax = dy*dy - dy*(dy+1)/2

"""
