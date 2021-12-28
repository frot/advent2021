#!/usr/bin/python3

"""
d = 3 .. 9

d: prob
[3: 1,
 4: 3,
 5: 6,
 6: 7
 7: 6
 8: 3
 9: 1]

sum: n * (1 + (start + d) % 10)

"""

import fileinput

pos = [int(line.strip().split(':')[1])-1 for line in fileinput.input()]

def play(p1, s1, p2, s2):
    if s2 >= 21:
        return 0,1

    w1 = 0
    w2 = 0
    for d,w in [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
        c2,c1 = play(p2,s2,(p1+d)%10,s1 + 1 + (p1+d)%10)
        w1 = w1 + w * c1
        w2 = w2 + w * c2

    return w1,w2

x = play(pos[0], 0, pos[1], 0)
print(max(x))
