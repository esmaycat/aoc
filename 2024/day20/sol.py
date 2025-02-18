# AOC 2024 Day 20 – expect input on stdin

import itertools

start, end, grid = -1, -1, {}
for y, l in enumerate(open(0).read().splitlines()):
    for x, c in enumerate(l):
        grid[complex(x, y)] = c
        if c == 'E': end = complex(x, y)
        elif c == 'S': start = complex(x, y)


track = {}
current = start
facing = 0
for t in itertools.count():
    track[current] = t
    if current == end:
        break

    for direction in 1, -1, 1j, -1j:
        next = current + direction
        if grid[next] != '#' and direction != -facing:
            facing, current = direction, next
            break

def count_cheats(maxcheats):
    n = 0
    for start, end in itertools.combinations(track, r=2):
        manhattan = abs(start.real-end.real) + abs(start.imag-end.imag)
        n += manhattan <= maxcheats and abs(track[end]-track[start])-manhattan >= 100
    return n

print(count_cheats(2))  # Part 1
print(count_cheats(20)) # Part 2
