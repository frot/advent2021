#!/usr/bin/python3

import fileinput

data = [int(x) for line in fileinput.input() for x in line.split(',')]
fish = [0] * 9
for d in data:
    fish[d] += 1

for gen in range(80):
    fish[(gen + 7) % 9] += fish[gen % 9]
    print(fish)

print(sum(fish))
