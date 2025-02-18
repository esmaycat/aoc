# AOC 2024 Day 8 – expect input on stdin 

from collections import defaultdict
from itertools import combinations

d = open(0).read().splitlines()
width = len(d[0])
frequencies = defaultdict(set)
for y, row in enumerate(d):
    for x, c in enumerate(row):
        if c not in '.\n': frequencies[c].add((x, y))

def valid(x, y):
    return 0 <= x < width and 0 <= y < len(d)

p1 = set()
p2 = set()
for freq, indices in frequencies.items():
    for (ax, ay), (bx, by) in combinations(indices, r=2):
        p2.add((ax, ay))
        p2.add((bx, by))

        dx, dy = bx-ax, by-ay
        
        px, py = ax-dx, ay-dy
        if valid(px, py): p1.add((px, py))
        while valid(px, py):
            p2.add((px, py))
            px -= dx; py -= dy

        qx, qy = bx+dx, by+dy
        if valid(qx, qy): p1.add((qx, qy))
        while valid(qx, qy):
            p2.add((qx, qy))
            qx += dx; qy += dy

print(len(p1)) # Part 1
print(len(p2)) # Part 2