from collections import defaultdict

secrets = [*map(int, open(0))]

def next_secret(n):
    n ^= n << 6
    n &= 16777215
    n ^= n >> 5
    n &= 16777215
    n ^= n << 11
    n &= 16777215
    return n

p1 = 0
sequences = defaultdict(int)

for s in secrets:
    prices = [s] + [s := next_secret(s) for _ in range(2000)]
    p1 += prices[-1]
    ones = [p%10 for p in prices]
    diffs = tuple(b-a for a, b in zip(ones, ones[1:]))

    seen = set()
    for i in range(len(diffs) - 4):
        seq = diffs[i:i+4]
        if seq not in seen:
            sequences[diffs[i:i+4]] += ones[i+4]
            seen.add(diffs[i:i+4])

print(p1)
print(max(sequences.values()))