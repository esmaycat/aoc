# AOC 2024 Day 5 – expect input on stdin 

import itertools
import typing

d = open(0).read()
width = d.index('\n')
length = len(d)

def patrol(d):
    directions = iter(itertools.cycle((-width-1, 1, width+1, -1)))
    direction = next(directions)

    position = d.index('^')
    seen = {position,}

    n_repeats = 0

    while 1:
        position += direction
        if position < 0 or position > length or d[position] == '\n':
            break
        if d[position] == '#':
            position -= direction
            direction = next(directions)
            continue
        n_repeats = (n_repeats+1)*(position in seen)
        if n_repeats >= width:
            return False
        
        seen.add(position)
    return seen

patrolled = typing.cast(set[int], patrol(d))
print(len(patrolled))                                     # Part 1
patrolled.remove(d.index('^'))
print(sum(not patrol(d[:position] + '#' + d[position+1:]) # Part 2
          for position in patrolled))