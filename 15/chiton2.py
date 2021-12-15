#!/usr/bin/python3

import fileinput
import sys
sys.setrecursionlimit(3000)

indata = [[int(c) for c in line.strip()] for line in fileinput.input()]
data = [[1+(c+yy+xx-1)%9 for xx in range(5) for c in row] for yy in range(5) for row in indata]
risk = [[99999 for col in row] for row in data]

rowmax = len(data)-1
colmax = len(data[0])-1
print(rowmax, colmax)

min_risk = 99999
def walk(row, col, r_path=0):
    global min_risk
    if 0<=row<=rowmax and 0<=col<=colmax:
        r_path += data[row][col]
        r_point = risk[row][col]
        if r_path<r_point and r_path<min_risk:
            risk[row][col] = r_path
            if row==rowmax and col==colmax:
                min_risk = r_path
                print(min_risk-1)
                return
            walk(row+1, col, r_path)
            walk(row, col+1, r_path)
            walk(row-1, col, r_path)
            walk(row, col-1, r_path)

walk(0, 0)
print(min_risk-1)
