from collections import Counter
from itertools import pairwise

from aoc_utils import window

secrets = map(int, open("inputs/day22.txt").read().splitlines())


def evolve(x):
    seq = [x]
    for _ in range(2000):
        x = ((x * 64) ^ x) % 16777216
        x = ((x // 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216
        seq.append(x)
    return seq


part1 = 0
part2 = Counter()
for secret in secrets:
    seq = evolve(secret)
    part1 += seq[-1]
    digits = [x % 10 for x in seq]
    diffs = (b - a for a, b in pairwise(digits))
    seen = set()
    for changes, price in zip(window(diffs, 4), digits[4:]):
        if changes not in seen:
            seen.add(changes)
            part2[changes] += price

print(part1)
print(part2.most_common(1)[0][1])
