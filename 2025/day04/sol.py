# AOC 2025 Day 4 – expect input on stdin

g: dict[complex, str] = {}
for y, line in enumerate(open(0)):
    for x, c in enumerate(line.strip()):
        g[complex(x, y)] = c

def remove(g: dict[complex, str] = g) -> int:
    tr = [
        i for i, c in g.items()
        if c == '@'
        if sum(
            g[d] == '@' for d in map(i.__add__, (1, -1, 1j, -1j, 1-1j, -1-1j, 1j-1, 1j+1))
            if d in g
        ) < 4
    ]
    for i in tr: del g[i]
    return len(tr)

print(remove(g.copy()))   # Part 1
print(sum(iter(remove, 0))) # Part 2
