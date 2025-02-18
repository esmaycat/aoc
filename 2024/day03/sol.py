# AOC 2024 Day 3 – expect input on stdin 

import re

d = open(0).read()

print(sum(eval(m.replace(',', '*')) # Part 1
      for m in re.findall(r'(?:mul\()(\d+,\d+)(?:\))', d)))

do = True
total = 0
mul = int.__mul__
for m in re.findall(r"do(?:n't)?\(\)|mul\(\d+,\d+\)", d):
    if m == 'do()':
        do = True
    elif m =='don\'t()':
        do = False
    elif do:
        total += eval(m)
print(total)                        # Part 2