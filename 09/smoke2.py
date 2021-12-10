#!/usr/bin/python3

import fileinput

data = [[9] + [int(c) for c in line.strip()] + [9] for line in fileinput.input()]

b = [9] * len(data[0])
data.insert(0, b)
data.append(b)

def fill1(row, col):
    """Simplest recursive 4-way"""
    if data[row][col]>=9:
        return 0
    data[row][col]=10
    return 1+fill(row,col-1)+fill(row,col+1)+fill(row-1,col)+fill(row+1,col)

def fill2(row, col):
    """Stack 4-way"""
    s = [(row,col)]
    count=0
    while len(s):
        r,c = s.pop()
        if data[r][c]<9:
            data[r][c]=10
            count+=1
            s.extend([(r,c-1), (r,c+1), (r-1,c), (r+1,c)])
    return count

def fill3(y, x):
    """Scan and fill"""
    def scan(lx, rx, y, s):
        a=False
        for x in range(lx, rx+1):
            if data[y][x]>=9:
                a=False
            elif not a:
                s.append((x, y))
                a=True
    if data[y][x]>=9:
        return 0
    s = [(x, y)]
    count=0
    while len(s):
        x,y = s.pop()
        lx = x
        while data[y][lx-1]<9:
            data[y][lx-1]=10
            count += 1
            lx -= 1
        while data[y][x]<9:
            data[y][x]=10
            count += 1
            x += 1
        scan(lx, x-1, y+1, s)
        scan(lx, x-1, y-1, s)
    return count

def fill4(y,x):
    """Optimized span fill"""
    if data[y][x]>=9:
        return 0
    s = [(x, x, y, 1), (x, x, y-1, -1)]
    count=0
    while len(s):
        x1, x2, y, dy = s.pop()
        x = x1
        if 0<=y<len(data) and data[y][x]<9:
            while data[y][x-1]<9:
                data[y][x-1]=10
                count += 1
                x -= 1
            if x<x1:
                s.append((x, x1-1, y-dy, -dy))
        while x1<x2 or data[y][x1]<9:
            while data[y][x1]<9:
                data[y][x1]=10
                count += 1
                x1 += 1
            if x<x1:
                s.append((x, x1-1, y+dy, dy))
            if (x1-1) > x2:
                s.append((x2+1, x1-1, y-dy, -dy))
            while x1<x2 and data[y][x1]>=9:
                x1 += 1
            x = x1
    return count

fill = fill4
sizes = []
for row,d in enumerate(data[1:-1], 1):
    for col,p in enumerate(d[1:-1], 1):
        nb = min(data[row-1][col], data[row+1][col], d[col-1], d[col+1])
        if p < nb:
            sizes.append(fill(row, col))

sizes.sort(reverse=True)
print(sizes)
print(sizes[0]*sizes[1]*sizes[2])
