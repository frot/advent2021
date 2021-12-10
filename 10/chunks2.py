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
        elif expect:
            if c != expect.pop():
                expect = []
                break
        else:
            break

    if expect:
        score = 0
        expect.reverse()
        for c in expect:
            score *= 5
            score += points[c]
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])
