# AOC 2024 Day 11 – expect input on stdin

from functools import cache
from math import log10, floor

stones = [*map(int, open(0).read().split())]

@cache
def rec(stone, depth, n=0):
    if n == depth:
        return 1

    if stone == 0:
        return rec(1, depth, n+1)
    elif (digits := floor(log10(stone)) + 1) % 2 == 0:
        p = pow(10, digits//2)
        return rec(stone % p, depth, n+1) + rec(stone // p, depth, n+1)
    return rec(stone * 2024, depth, n+1)

print(sum(rec(stone, 25) for stone in stones)) # Part 1
print(sum(rec(stone, 75) for stone in stones)) # Part 2
