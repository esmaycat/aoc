# AOC 2024 Day 8 – expect input on stdin

from itertools import repeat, chain

d = open(0).read()

p1 = [*chain.from_iterable(repeat((i//2,'.')[i%2], int(c)) for i, c in enumerate(d))]
print(p1)
blocks = len(p1)-p1.count('.')
iterations = p1[:blocks].count('.')
front, back = 0, -1

while iterations:
    if p1[back] == '.': back -= 1; continue
    if p1[front] != '.': front += 1; continue
    p1[front] = p1[back]
    front += 1; back -= 1; iterations -= 1

print(sum(i*int(c)for i, c in enumerate(p1[:blocks]) if c != '.')) # Part 1

p2 = [*map(int, d)]
files, spaces = p2[::2], p2[1::2]
taken = [0] * len(spaces)

a = [0] * sum(p2)

for n1, file in enumerate(files[::-1]):
    n1 = len(files) - n1 - 1
    for n2, space in enumerate(spaces):
        if space >= file and n1>n2:
            i = sum(p2[:n2*2+1]) + taken[n2]
            a[i:i+file] = [n1]*file
            taken[n2] += file
            spaces[n2] -= file
            break
    else:
        i = sum(p2[:n1*2])
        a[i:i+file] = [n1]*file

print(sum(i*c for i, c in enumerate(a)))                           # Part 2
