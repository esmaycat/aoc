# AOC 2024 Day 16 – expect input on stdin

import heapq
from dataclasses import dataclass, field

@dataclass(order=True)
class Node:
    pos: int = field(compare=False)
    facing: int = field(compare=False)
    path: list[int] = field(compare=False)
    score: int

d = open(0).read()
width = d.index('\n') + 1
start = d.index('S')
end = d.index('E')

queue = [Node(pos=start, facing=1, path=[start], score=0)]
seen = {(start, 1): 0}
lowest = float('inf')
paths = []

while queue:
    node = heapq.heappop(queue)

    for direction in (1, -1, -width, width):
        next = node.pos + direction
        if direction == -node.facing: continue
        if d[next] == '#': continue
        if next in node.path: continue

        score = node.score + (1001 if abs(direction) != abs(node.facing) else 1)
        if (next, direction) in seen and score > seen[next, direction]: continue

        if next == end:
            paths.append(node.path)
            if score < lowest:
                lowest = score
            continue

        if score < lowest:
            seen[next, direction] = score
            heapq.heappush(queue, Node(pos=next, score=score, facing=direction, path=node.path + [next]))

print(lowest)                               # Part 1
print(len(set.union(*map(set, paths))) + 1) # Part 2
