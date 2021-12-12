#!/usr/bin/python3

import fileinput

data = [[int(c) for c in line.strip()] for line in fileinput.input()]

def check(row, col):
    if 0<=row<len(data) and 0<=col<len(data[0]):
        data[row][col] += 1
        if data[row][col] == 10:
            check(row-1, col-1)
            check(row-1, col)
            check(row-1, col+1)
            check(row,   col-1)
            check(row,   col+1)
            check(row+1, col-1)
            check(row+1, col)
            check(row+1, col+1)

def pprint(d):
    for r in data:
        print(''.join([str(c) for c in r]))

count = 0
for step in range(100):
    for row in range(len(data)):
        for col in range(len(data[0])):
            check(row, col)
    for row in data:
        for col,c in enumerate(row):
            if c>9:
                count += 1
                row[col] = 0
    #pprint(data)
    #print(count)

print(count)
