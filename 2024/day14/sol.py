# AOC 2024 Day 14 – expect input on stdin 

import re, math, collections, itertools

d = [[*map(int, re.findall(r'-?\d+', l))] for l in open(0)]

if len(d) > 12:
    w, h = 101, 103
else:
    w, h = 11, 7

def sim(s=100):
    q = [0, 0, 0, 0]
    p = collections.defaultdict(set)

    for x, y, vx, vy in d:
        nx, ny = (x+vx*s)%w, (y+vy*s)%h
        p[ny].add(nx)
        if nx == w//2 or ny == h//2: continue
        q[(nx >= w//2) + (ny >= h//2)*2] += 1

    return q, p

def run(s):
    r = rmax = 0
    for i in range(w):
        if i in s:
            r += 1
            if r > rmax: rmax = r
        else: r = 0
    return rmax

print(math.prod(sim()[0])) # Part 1

if len(d) < 12: exit()

for secs in itertools.count(1):
    _, p = sim(secs)
    if any(run(p[y]) > 10 for y in p):
        print('\n'.join(''.join('##' if i in p[j] else '..' for i in range(w)) for j in range(h)))
        print(secs)        # Part 2
        break