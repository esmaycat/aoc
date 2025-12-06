# AOC 2025 Day 5 – expect input on stdin

b, ingredients = open(0).read().split('\n\n')
ranges = sorted(map(eval, b.replace('-', ',').split('\n')))
ingredients = [*map(int, ingredients.split('\n'))]

print(sum(any(a <= i <= b for a, b in ranges) for i in ingredients)) # Part 1

p2 = 0
a, b = ranges[0]
for p, q in ranges[1:]:
    if p > b:
        p2 += b - a + 1
        a, b = p, q
    else: b = max(b, q)

print(p2 + b - a + 1)                                                # Part 2
