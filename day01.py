from collections import Counter
from itertools import batched

lines = open("inputs/day01.txt").read().strip()

l, r = zip(*batched(map(int, lines.split()), 2))
print(sum(abs(a - b) for a, b in zip(sorted(l), sorted(r))))

count = Counter(r)
print(sum(a * count.get(a, 0) for a in l))
