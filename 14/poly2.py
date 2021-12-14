#!/usr/bin/python3

import fileinput
from collections import defaultdict

fi = fileinput.input()

tmpl = [c for c in next(fi).strip()]
next(fi)

rules = {k: [k[0]+v, v+k[1], v] for k,v in [line.strip().split(' -> ') for line in fi]}

count = defaultdict(int)
for c in tmpl:
    count[c] += 1

pairs = defaultdict(int)
for p in zip(tmpl, tmpl[1:]):
    pairs[''.join(p)] += 1

for step in range(40):
    pnew = defaultdict(int)
    for p,v in pairs.items():
        p1,p2,c = rules[p]
        pnew[p1] += v
        pnew[p2] += v
        count[c] += v
    pairs = pnew

count = sorted(count.items(), key=lambda a: a[1])
print(count[0])
print(count[-1])
print(count[-1][1] - count[0][1])
