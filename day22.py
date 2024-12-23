from collections import defaultdict
from itertools import pairwise

secrets = map(int, open("inputs/day22.txt").read().splitlines())


def evolve(x):
    x = (x << 6 ^ x) % 16777216
    x = (x >> 5 ^ x) % 16777216
    return (x << 11 ^ x) % 16777216


part1 = 0
part2 = defaultdict(int)

for secret in secrets:
    seq = [secret] + [secret := evolve(secret) for _ in range(2000)]
    part1 += seq[-1]
    digits = [x % 10 for x in seq]
    diffs = [b - a + 9 for a, b in pairwise(digits)]
    seen = set()
    for i in range(len(digits) - 4):
        key = diffs[i] * 19**3 + diffs[i + 1] * 19**2 + diffs[i + 2] * 19 + diffs[i + 3]
        if key not in seen:
            seen.add(key)
            part2[key] += digits[4 + i]

print(part1)
print(max(part2.values()))
