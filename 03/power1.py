#!/usr/bin/python3

import fileinput
from functools import reduce

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
data = [[c for c in line] for line in fileinput.input()]
bits = reduce(lambda bb,xx: [b+int(x) for b,x in zip(bb, xx)] , data, [0]*12)
count = len(data)/2

print(''.join(['1' if b > count else '0' for b in bits]))
gamma = int(''.join(['1' if b > count else '0' for b in bits]), base=2)
epsilon = ~gamma & 0b111111111111

print(gamma,epsilon)
print(gamma*epsilon)
