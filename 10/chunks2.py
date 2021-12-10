#!/usr/bin/python3

import fileinput

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
    }

scores = []
for line in fileinput.input():
    expect = []
    for c in line.strip():
        i = '([{<'.find(c)
        if i >= 0:
            expect.append(')]}>'[i])
        elif c != expect.pop():
            break
    else:
        score = 0
        while expect:
            score *= 5
            score += points[expect.pop()]
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])
