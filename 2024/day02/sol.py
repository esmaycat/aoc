# AOC 2024 Day 2 – expect input on stdin 

d = [[*map(int, l.split())] for l in open(0)]

def safe(l):
    d = [a-b for a, b in zip(l, l[1:])]
    m = 2*(d[0]>0)-1
    return all(0 < m*i < 4 for i in d)

print(sum(safe(l) for l in d))               # Part 1
print(sum(safe(l) or any(safe(l[:i]+l[i+1:]) # Part 2
      for i in range(len(l))) for l in d))