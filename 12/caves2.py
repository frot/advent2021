#!/usr/bin/python3

import fileinput
from collections import defaultdict

data = [line.strip().split('-') for line in fileinput.input()]

conn = defaultdict(list)
for d in data:
    conn[d[0]].append(d[1])
    conn[d[1]].append(d[0])

count = 0
def check(pos, path, dd):
    global count
    for dest in conn[pos]:
        if dest == 'end':
            #print(path + [dest])
            count += 1
        elif dest.isupper() or dest not in path:
            check(dest, path + [dest], dd)
        elif dest != 'start' and not dd:
            check(dest, path + [dest], True)

check('start', path=['start'], dd=False)
print(count)
