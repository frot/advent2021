#!/usr/bin/python3

import fileinput
from functools import reduce
from operator import ge, lt

test = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

# data = [[c for c in line] for line in test]
data = [[c for c in line.strip()] for line in fileinput.input()]

def filter1(data, op):
    for pos in range(len(data[0])):
        bits = reduce(lambda bb,xx: [b+int(x) for b,x in zip(bb, xx)] , data, [0]*len(data[0]))
        count = len(data)/2
        gamma = ['1' if op(b, count) else '0' for b in bits]
        data = [b for b in data if b[pos] == gamma[pos]]
        if len(data) == 1:
            return int(''.join(data[0]), base=2)
    else:
        print("Foo!")
        return 0

ox = filter1(data, ge)
co = filter1(data, lt)

print(ox,co)
print(ox*co)
