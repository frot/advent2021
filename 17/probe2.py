#!/usr/bin/python3

import re
import fileinput

def shoot(x1, x2, y1, y2):
    print(x1, x2, y1, y2)

    xs=[]
    for dx in range(1, x2+1):
        for n in range(dx):
            x = dx*(n+1) - n*(n+1)/2
            if x1<=x<=x2:
                xs.append((n, dx, (n == (dx-1))))

    dy = -y1-1
    ymax = dy*(dy + 1)//2
    ys=[]
    for dy in range(y1, ymax+1):
        for n in range(1000):
            y = dy*(n+1) - n*(n+1)/2
            if y1<=y<=y2:
                ys.append((n, dy))

    count=0
    uniq = set()
    for nx,x,e in xs:
        for ny,y in ys:
            if nx==ny or (e and nx<=ny):
                if (x,y) not in uniq:
                    uniq.add((x,y))
                    count+=1

    print(count)

for line in fileinput.input():
    m = re.search(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line)
    shoot(int(m[1]), int(m[2]), int(m[3]), int(m[4]))


"""
x = dx*(n+1) - n*(n+1)/2

x = dx*(dx+1) - dx*(dx+1)/2
x = dx*dx + dx - dx*dx/2 + dx/2

d = dy - n

d = dy - 2*dy - 1

d = -dy - 1

-d-1 = dy

ymax = dy*dy - dy*(dy+1)/2

"""
