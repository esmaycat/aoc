# AOC 2024 Day 18 – expect input on stdin

import heapq
from dataclasses import dataclass, field

@dataclass(order=True)
class Node:
    pos: tuple[int, int] = field(compare=False)
    path: list[tuple[int, int]] = field(compare=False)
    steps: int

lines = open(0).read().splitlines()

if len(lines) > 25:
    w = h = 71
    lim = 1024
else:
    w = h = 7
    lim = 12

grid = {(x, y): '.' for y in range(h) for x in range(w)}
for line in lines[:lim]:
    grid[eval(line)] = '#'

def shortest_path():
    queue = [Node(steps=0, pos=(0, 0), path=[(0, 0)])]
    seen = set()

    while queue:
        node = heapq.heappop(queue)
        x, y = node.pos

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (nx, ny) == (w-1, h-1): return node
            if grid.get((nx, ny)) != '.': continue
            steps = node.steps + 1
            if (nx, ny) in seen: continue
            heapq.heappush(queue, Node(steps=steps, pos=(nx, ny), path=node.path + [(nx, ny)]))
            seen.add((nx, ny))

    return None

node = shortest_path()
print(node.steps + 1)   # Part 1

for line in lines[lim:]:
    p = eval(line)
    grid[p] = '#'
    if p in node.path:
        node = shortest_path()
        if node is None:
            print(line) # Part 2
            break
