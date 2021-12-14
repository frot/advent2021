#!/usr/bin/python3

import fileinput
from collections import defaultdict

fi = fileinput.input()

tmpl = [c for c in next(fi).strip()]
next(fi)

rules = {k: [k[0], v] for k,v in [line.strip().split(' -> ') for line in fi]}

for step in range(10):
    tmpl = [c for pair in zip(tmpl, tmpl[1:]) for c in rules.get(''.join(pair), [pair[0]])] + [tmpl[-1]]

print(len(tmpl))
count = defaultdict(int)
for c in tmpl:
    count[c] += 1

count = sorted(count.items(), key=lambda a: a[1])
print(count[0])
print(count[-1])
print(count[-1][1] - count[0][1])
