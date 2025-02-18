# AOC 2024 Day 7 – expect input on stdin 

import itertools

d = [(int(l), [*map(int, r.split())]) for l, r in map(lambda l: l.split(':'), open(0))]

def mul(x, y):
    return x//y if x%y == 0 else None

def add(x, y):
    return x-y if x-y > 0 else None

def concat(x, y):
    x, y = str(x), str(y)
    return int(x.removesuffix(y)) if x.endswith(y) and x != y else None

ops = [add, mul]

def evaluate(seq, perm, target):
    s = target
    for n in seq[:0:-1]:
        s = next(perm)(s, n)
        if s is None:
            return 0
    return s == seq[0]

def check(target, seq):
    perms = itertools.product(ops, repeat=len(seq) - 1)
    return target*any(evaluate(seq, iter(p), target) for p in perms)

print(sum(check(k, v) for k, v in d)) # Part 1
ops.append(concat)
print(sum(check(k, v) for k, v in d)) # Part 2