#!/usr/bin/python3

import fileinput

data = [[seg.split() for seg in line.split('|')] for line in fileinput.input()]

def cmp(s1, s2):
    return len([c for c in s1 if c in s2])

n = 0
for pat,out in data:
    lookup = {}
    for d in sorted(pat, key=len):
        dstr = ''.join(sorted(d))
        if len(dstr) == 2:
            lookup[dstr] = '1'
        elif len(dstr) == 3:
            lookup[dstr] = '7'
            acf = dstr
        elif len(dstr) == 4:
            lookup[dstr] = '4'
            bcdf = dstr
        elif len(dstr) == 5:
            if cmp(acf, dstr) == 3:
                lookup[dstr] = '3'
            elif cmp(bcdf, dstr) == 3:
                lookup[dstr] = '5'
            else:
                lookup[dstr] = '2'
        elif len(dstr) == 6:
            if not cmp(acf, dstr) == 3:
                lookup[dstr] = '6'
            elif cmp(bcdf, dstr) == 4:
                lookup[dstr] = '9'
            else:
                lookup[dstr] = '0'
        elif len(dstr) == 7:
            lookup[dstr] = '8'

    n += int(''.join([lookup[''.join(sorted(d))] for d in out]))

print(n)
