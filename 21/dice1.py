#!/usr/bin/python3

import fileinput

pos = [int(line.strip().split(':')[1])-1 for line in fileinput.input()]
score = [0, 0]
n = 0

while max(score) < 1000:
    d = 1+(3*n)%100 + 1+(1+3*n)%100 + 1+(2+3*n)%100
    pos[n%2] = (pos[n%2] + d) % 10
    score[n%2] += pos[n%2]+1
    n += 1

print(3*n*min(score))
