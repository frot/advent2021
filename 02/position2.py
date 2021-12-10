#!/usr/bin/python3

import fileinput
from functools import reduce

cmd = {
    'forward': (1, 0, 1),
    'up': (0, -1, 0),
    'down': (0, 1, 0)
}

data = [(k, int(v)) for k, v in [line.split() for line in fileinput.input()]]

pos = reduce(lambda p, d: [x+y*z*q for x,y,z,q in zip(p, cmd[d[0]], [d[1]]*3, (1, 1, p[1]))], data, (0, 0, 0))

print(pos[0]*pos[2])
