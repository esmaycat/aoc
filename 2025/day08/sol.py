from collections import defaultdict
from itertools import combinations
from heapq import nlargest
from functools import reduce
from math import dist

*boxes, = map(eval, open(0))
connections = {i: i for i in range(len(boxes))}

def find(n):
    if connections[n] != n: connections[n] = find(connections[n])
    return connections[n]

def get_sets():
    circuits = defaultdict(list)
    for n in range(len(boxes)):
        circuits[find(n)].append(n)
    return list(circuits.values())

connection_count = 0
for b1, b2 in sorted(combinations(range(len(boxes)), 2), key=lambda x: dist(boxes[x[0]], boxes[x[1]])):
    x, y = find(b1), find(b2)
    connections[x] = y
    connection_count += 1
    if connection_count == 1000: 
        print(reduce(int.__mul__, (nlargest(3, map(len, get_sets())))))
    # TODO: improve this, make it update when I update it :)
    for x in connections:find(x)
    if len(set(connections.values())) == 1:
        print(boxes[b1][0] * boxes[b2][0])
        break