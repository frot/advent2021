#!/usr/bin/python3

import fileinput

indata = [[int(c) for c in line.strip()] for line in fileinput.input()]
data = [[1+(c+yy+xx-1)%9 for xx in range(5) for c in row] for yy in range(5) for row in indata]
risk = [[99999 for col in row] for row in data]

rowmax = len(data)-1
colmax = len(data[0])-1
print(rowmax, colmax)

for i in range(20):
    for row,r in enumerate(data):
        for col,c in enumerate(r):
            if row>0 or col>0:
                w = c + risk[row][col-1] if col>0 else 99999
                n = c + risk[row-1][col] if row>0 else 99999
                e = c + risk[row][col+1] if col<colmax else 99999
                s = c + risk[row+1][col] if row<rowmax else 99999
                r = min(w, n, e, s)
            else:
                r = 1
            if r < risk[row][col]:
                risk[row][col] = r
    min_risk= risk[-1][-1]
    print(min_risk-1)
