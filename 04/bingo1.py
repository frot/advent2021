#!/usr/bin/python3

import fileinput
from functools import reduce
from pprint import pprint

fi = fileinput.input()
first = next(fi)
numbers = [int(c) for c in first.split(',')]

boards = []
board = []
for line in fi:
    row = line.split()
    if len(row) == 5:
        board.append([int(i) for i in row])
    if len(board) == 5:
        boards.append(board)
        board = []

def check(b, n):
    return n * sum([col for row in b for col in row if col<100])

def play():
    for n in numbers:
        for b in boards:
            for row in b:
                for x,col in enumerate(row):
                    if col == n:
                        row[x] += 100
                        if all([i>=100 for i in row]):
                            print("Bingo!")
                            return check(b, n)
                        elif all([r[x]>=100 for r in b]):
                            print("Bnigo!")
                            return check(b, n)

print(play())
