# AOC 2024 Day 5 – expect input on stdin 

from collections import Counter

top, bottom = open(0).read().split('\n\n')
rules = [(int(l[:2]), int(l[3:])) for l in top.split()]
updates = [eval(l) for l in bottom.split()]

p1 = p2 = 0

for update in updates:
    applicable = {rule for rule in rules if set(update) >= {*rule}}
    c1 = Counter(rule[0] for rule in applicable)
    c2 = Counter(i for rule in applicable for i in rule)
    c3 = {k: c1[k]/c2[k] for k in c2}
    s = tuple(sorted(update, key=lambda x: -c3[x]))
    mid = s[len(update)//2]
    if update == s:
        p1 += mid
    else:
        p2 += mid

print(p1) # Part 1
print(p2) # Part 2