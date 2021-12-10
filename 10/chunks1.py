#!/usr/bin/python3

import fileinput

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }

score = 0
expect = []
for line in fileinput.input():
    for c in line.strip():
        i = '([{<'.find(c)
        if i >= 0:
            expect.append(')]}>'[i])
        elif expect:
            if c != expect.pop():
                score += points[c]
                break
        else:
            break

print(score)
