#!/usr/bin/python3

import fileinput
from bitstring import ConstBitStream

def parse(b, npackets=1):
    vsum=0
    while b.pos < len(b) and npackets:
        v = b.read('uint:3')
        vsum += v
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
                vsum += parse(b, length)
            else:
                length = b.read('uint:15')
                vsum += parse(b.read(f'bits:{length}'), -1)
        npackets -= 1
    return vsum

for line in fileinput.input():
    print(line.strip())
    print(parse(ConstBitStream(hex=line)))
