#!/usr/bin/python3

import fileinput

data = sorted([int(x) for line in fileinput.input() for x in line.split(',')])
#print(data)

mp = len(data) // 2
if mp * 2 == len(data):
    mid = sum(data[mp-1:mp+1]) / 2
else:
    mid = data[mp]

print(mid)

fuel = 0
for d in data:
    fuel += abs(d - mid)

print(fuel)
