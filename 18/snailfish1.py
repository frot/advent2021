#!/usr/bin/python3

import fileinput

def explode(num):
    d=0
    li=None
    nn=None
    i=0
    while i < len(num):
        if num[i]=='[':
            d += 1
            if d>4 and nn is None:
                nn = num[i:i+5]
                if li:
                    num[li] += nn[1]
                nn = nn[3]
                num[i:i+5] = [0]
                d -= 1
        elif num[i]==']':
            d -= 1
        elif isinstance(num[i], int):
            if nn is not None:
                num[i] += nn
                return True
            li = i
        i += 1
    else:
        return False

def split(num):
    for i,n in enumerate(num):
        if isinstance(n, int) and n>9:
            num[i:i+1] = ['[', n//2, ',', (n+1)//2, ']']
            return True
    else:
        return False

def red(num):
    while True:
        while True:
            if not explode(num):
                break
        if not split(num):
            break

def mag(num):
    if isinstance(num[0], int):
        n1 = num[0]
    else:
        n1 = mag(num[0])
    if isinstance(num[1], int):
        n2 = num[1]
    else:
        n2 = mag(num[1])
    return 3*n1 + 2*n2

num = None
for line in fileinput.input():
    expr = [int(c) if c.isdigit() else c for c in line.strip()]
    if num:
        num = ['['] + num + [','] + expr + [']']
    else:
        num = expr
    print("In:", ''.join([str(c) for c in num]))
    red(num)
    print("Rd:", ''.join([str(c) for c in num]))
    print("Mag:", mag(eval(''.join([str(c) for c in num]))))
