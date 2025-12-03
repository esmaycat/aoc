# AOC 2025 Day 2 – expect input on stdin

ranges = [(*map(int, r.split('-')),) for r in open(0).read().split(',')]
p1 = p2 = 0
for a, b in ranges:
    lenid = len(str(a))
    for id in range(a, b + 1):
        sid = str(id)
        if sid[:lenid//2]*2 == sid:
            p1 += id
            continue 
    
        for s in range(1, lenid // 2 + 1):
            if sid[:s]*(lenid // s) == sid:
                break
        else:
            continue
        p2 += id

print(p1)      # Part 1
print(p2 + p1) # Part 2