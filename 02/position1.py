#!/usr/bin/python3

import fileinput

cmd = {
    'forward': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}

data = [(k, int(v)) for k, v in [line.split() for line in fileinput.input()]]

pos = (0, 0)
for k,v in data:
    pos = tuple(x+y*z for x,y,z in zip(pos, cmd[k], (v, v)))

print(pos[0],pos[1])
