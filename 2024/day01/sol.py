# AOC 2024 Day 1 – expect input on stdin 

l, r = zip(*[map(int, p.split()) for p in open(0)])
print(sum(abs(a-b) for a, b in zip(sorted(l), sorted(r)))) # Part 1
print(sum(a*r.count(a) for a in l))                        # Part 2