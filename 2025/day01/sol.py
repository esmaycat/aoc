# AOC 2025 Day 1 – expect input on stdin

rs = [int(l.translate({82: '+', 76: '-'})) for l in open(0)]
dial = 50
p1 = p2 = 0
for r in rs:
    at_zero = dial == 0
    s, dial = divmod(dial + r, 100)
    p2 += abs(s)
    if r < 0: p2 += (dial == 0) - at_zero
    p1 += dial == 0

print(p1) # Part 1
print(p2) # Part 2