# AOC 2024 Day 5 – expect input on stdin 

import re

def solve(ax, ay, bx, by, px, py):
    d, k, u = ax*by - bx*ay, px*by - bx*py, ax*py - px*ay
    return 0 if k % d or u % d else (k//d)*3 + u//d

p1 = p2 = 0
for c in open(0).read().split('\n\n'):
    *coefs, px, py = map(int, re.findall(r'\d+', c))
    p1 += solve(*coefs, px, py) # type: ignore
    p2 += solve(*coefs, px+10000000000000, py+10000000000000) # type: ignore

print(p1) # Part 1
print(p2) # Part 2