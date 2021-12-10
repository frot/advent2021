#!/usr/bin/python3

import fileinput

lookup = [
    0,  # 0: ' '
    0,  # 1: n/a
    1,  # 2: '1'
    1,  # 3: '7'
    1,  # 4: '4'
    0,  # 5: '2', '3', '5'
    0,  # 6: '0', '6', '9'
    1   # 7: '8'
]

data = [[seg.split() for seg in line.split('|')] for line in fileinput.input()]
#print(data)

count = 0
for pat,out in data:
    for d in out:
        count += lookup[len(d)]

print(count)
