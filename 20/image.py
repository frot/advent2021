#!/usr/bin/python3

import fileinput

tr = str.maketrans('.#', '01')
rt = str.maketrans('01', '.#')
fi = fileinput.input()
ie = next(fi).strip().translate(tr)
next(fi)
img = [line.strip().translate(tr) for line in fi]

def extend(im, x=2, c=None):
    if c is None:
        c=im[0][0]
    w = len(im[0])+2*x
    return [c*w for i in range(x)] + [c*x + r + c*x for r in im] + [c*w for i in range(x)]

def process(im):
    return [''.join([ie[int(im[r][c:c+3]+im[r+1][c:c+3]+im[r+2][c:c+3], base=2)] for c in range(len(im[r])-2)]) for r in range(len(im)-2)]

def pprint(im):
    s = '\n'.join([r.translate(rt) for r in im])
    print(s)
    print(s.count('#'))

n = 50
print(n)
img = extend(img,3,'0')
for i in range(n):
    img = extend(img,2)
    img = process(img)
    pprint(img)
    print()
