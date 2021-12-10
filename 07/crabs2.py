#!/usr/bin/python3

import fileinput

data = sorted([int(x) for line in fileinput.input() for x in line.split(',')])

mean = sum(data)/len(data)
print(mean)

mp = len(data) // 2
if mp * 2 == len(data):
    mid = int(sum(data[mp-1:mp+1]) / 2)
else:
    mid = int(data[mp])

print(mid)

def calc(m):
    f = 0
    for d in data:
        dist = abs(d - m)
        f += dist * (dist+1) / 2
    return f

minp = mid
minf = calc(mid)
for p in range(minp, len(data), 1):
    f = calc(p)
    if f > minf:
        print(minp, minf)
        break;
    minp = p
    minf = f
