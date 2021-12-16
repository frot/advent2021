#!/usr/bin/python3

import fileinput
from bitstring import ConstBitStream

opers=[
    lambda a,b: a+b,
    lambda a,b: a*b,
    min,
    max,
    None,
    lambda a,b: 1 if a>b else 0,
    lambda a,b: 1 if a<b else 0,
    lambda a,b: 1 if a==b else 0,
]    

def parse(b, npackets=1, op=opers[0]):
    expr=None
    while b.pos < len(b) and npackets:
        v = b.read('uint:3')
        t = b.read('uint:3')
        #print('packet', v, t)
        if t==4:
            n = 0
            cont = True
            while cont:
                cont = b.read('bool')
                n = (n<<4) + b.read('uint:4')
        else:
            if b.read('bool'):
                length = b.read('uint:11')
                n = parse(b, length, opers[t])
            else:
                length = b.read('uint:15')
                n = parse(b.read(f'bits:{length}'), -1, opers[t])
        if expr is None:
            expr = n
        else:
            expr = op(expr, n)
        npackets -= 1
    return expr

for line in fileinput.input():
    print(line.strip())
    print(parse(ConstBitStream(hex=line)))
