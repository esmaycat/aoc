# AOC 2024 Day 19 – expect input on stdin

from functools import cache

towels, designs = open(0).read().split('\n\n')
towels = towels.split(', ')
designs = designs.split('\n')

@cache
def valid(d):
    return not d or sum(valid(d[len(t):]) for t in towels if d.startswith(t))

print(sum(valid(d)>0 for d in designs)) # Part 1
print(sum(map(valid, designs)))         # Part 2
