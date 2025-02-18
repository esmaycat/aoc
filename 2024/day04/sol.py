# AOC 2024 Day 4 – expect input on stdin 

d = open(0).read()
w = d.index('\n') + 1
print(sum(d[i::p][:4] in ('XMAS', 'SAMX')                     # Part 1
      for i in range(len(d)) for p in (1, w, w+1, w-1)))
print(sum({d[i-p::p][:3] for p in(w-1, w+1)} <= {'SAM','MAS'} # Part 2
      for i in range(len(d))))