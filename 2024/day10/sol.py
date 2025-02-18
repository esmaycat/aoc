# AOC 2024 Day 10 – expect input on stdin 

r = open(0).read()
w = r.index('\n')
d = [int(c) for c in r if c != '\n']

p1 = p2 = 0

for i, height in enumerate(d):
    if height != 0: continue
    search = [(i%w, i//w, height)]
    seen = set()

    while search:
        x, y, height = search.pop()

        for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < w and 0 <= ny < len(d)//w): continue
            nh = d[ny*w+nx]
            if nh != height + 1: continue
            search.append((nx, ny, nh))

            if nh == 9: 
                p1 += not (nx, ny) in seen
                p2 += 1

            seen.add((nx, ny))

print(p1) # Part 1
print(p2) # Part 2