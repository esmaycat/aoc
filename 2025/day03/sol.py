# AOC 2025 Day 3 – expect input on stdin

import operator as op

banks = [[*map(int, b.strip())] for b in open(0)]
p1 = p2 = 0 

def joltage(b: list[int], n: int) -> int:
    r = idx = 0
    for i in range(-n + 1, 1):
        idx, m = max(enumerate(b[idx:i or None], idx), key=op.itemgetter(1))
        idx += 1
        r += m * 10**-i
    return r

for b in banks:
    p1 += joltage(b, 2)
    p2 += joltage(b, 12)
                
print(p1) # Part 1
print(p2) # Part 2
