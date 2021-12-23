#!/usr/bin/python3

import fileinput
from pprint import pprint

fi = fileinput.input()

sc_data = []
sc_meta = []
sc_dist = []
for sc_line in fi:
    if sc_line.startswith("--- scanner "):
        sc_num = int(sc_line[12:14])
        sc_data.append([])
        sc_meta.append([])
    else:
        continue

    for pr_line in fi:
        if ',' in pr_line:
            sc_data[sc_num].append(tuple(int(s) for s in pr_line.split(',')))
        else:
            break
        
    n = len(sc_data[sc_num])
    sc_meta[sc_num] = [[0] * n for s in range(n)]
    for i0,p0 in enumerate(sc_data[sc_num][:-1]):
        for i1,p1 in enumerate(sc_data[sc_num][i0+1:], i0+1):
            dist = abs(p0[0] - p1[0]) + abs(p0[1] - p1[1]) + abs(p0[2] - p1[2])
            sc_meta[sc_num][i0][i1] = dist
            sc_meta[sc_num][i1][i0] = dist

trans = [
    lambda x,y,z: (x, y, z),
    lambda x,y,z: (x, -z, y),
    lambda x,y,z: (x, -y, -z),
    lambda x,y,z: (x, z, -y),
    lambda x,y,z: (-y, x, z),
    lambda x,y,z: (z, x, y),
    lambda x,y,z: (y, x, -z),
    lambda x,y,z: (-z, x, -y),
    lambda x,y,z: (-x, -y, z),
    lambda x,y,z: (-x, -z, -y),
    lambda x,y,z: (-x, y, -z),
    lambda x,y,z: (-x, z, y),
    lambda x,y,z: (y, -x, z),
    lambda x,y,z: (z, -x, -y),
    lambda x,y,z: (-y, -x, -z),
    lambda x,y,z: (-z, -x, y),
    lambda x,y,z: (-z, y, x),
    lambda x,y,z: (y, z, x),
    lambda x,y,z: (z, -y, x),
    lambda x,y,z: (-y,-z, x),
    lambda x,y,z: (-z, -y, -x),
    lambda x,y,z: (-y, z, -x),
    lambda x,y,z: (z, y, -x),
    lambda x,y,z: (y, -z, -x),
]

def search():
    print("============")
    for sc1_num,sc1 in enumerate(sc_data[1:], 1):
        matched = []
        for p1_num,p1 in enumerate(sc1):
            for p0_num,p0 in enumerate(sc_data[0]):
                for p1_i,d1 in enumerate(sc_meta[sc1_num][p1_num]):
                    for p0_i,d0 in enumerate(sc_meta[0][p0_num]):
                        if d0 and d1 and d0 == d1:
                            p01 = sc_data[0][p0_i]
                            p11 = sc1[p1_i]
                            matched.append((p0, p01, p1, p11))
        print("matched", len(matched))
        for tr_i, tr in enumerate(trans):
            matched2 = []
            for p0, p01, p1, p11 in matched:
                if (p01[0]-p0[0], p01[1]-p0[1], p01[2]-p0[2]) == tr(p11[0]-p1[0], p11[1]-p1[1], p11[2]-p1[2]):
                    matched2.append((p0, p1))
                    if len(matched2)>10:
                        print(sc1_num)
                        print(p0, p1, tr(*p1))
                        tr_p1 = tr(*p1)
                        dt = (p0[0]-tr_p1[0], p0[1]-tr_p1[1], p0[2]-tr_p1[2])
                        sc_dist.append(dt)
                        print(tr_i, dt)
                        print(p0, p1, tr(*p1))
                        for t1_num,t1 in enumerate(sc1):
                            pp1 = tr(*t1)
                            pp2 = (pp1[0]+dt[0], pp1[1]+dt[1], pp1[2]+dt[2])
                            if pp2 not in sc_data[0]:
                                sc_data[0].append(pp2)
                                sc_meta[0].append([0] * len(sc_data[0]))
                                ii0 = len(sc_data[0])-1
                                for ii1, ppp1 in enumerate(sc_data[0][:-1]):
                                    dist = abs(pp2[0] - ppp1[0]) + abs(pp2[1] - ppp1[1]) + abs(pp2[2] - ppp1[2])
                                    sc_meta[0][ii0][ii1] = dist
                                    sc_meta[0][ii1].append(dist)
                        del sc_data[sc1_num]
                        del sc_meta[sc1_num]
                        return
    print("FAIL!")
    exit(1)

while len(sc_data)>1:
    search()

#pprint(sorted(sc_data[0]))
print(len(sc_data[0]))
print(sc_dist)
maxdist = 0
for i0,d0 in enumerate(sc_dist):
    for d1 in sc_dist[i0+1:]:
        maxdist = max(maxdist, abs(d1[0]-d0[0]) + abs(d1[1]-d0[1]) + abs(d1[2]-d0[2]))
print(maxdist)
