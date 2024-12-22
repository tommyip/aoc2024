from itertools import pairwise

from tqdm import tqdm

from aoc_utils import window

inputs = map(int, open("inputs/day22.txt").read().splitlines())


def evolve(x):
    seq = [x]
    for _ in range(2000):
        x = ((x * 64) ^ x) % 16777216
        x = ((x // 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216
        seq.append(x)
    return seq


secrets = [evolve(x) for x in inputs]

print(sum(s[-1] for s in secrets))

digits = [[x % 10 for x in seq] for seq in secrets]
diffs = [[b - a for a, b in pairwise(seq)] for seq in digits]
num_maps = []
changes = set()
for seq, diff in zip(digits, diffs):
    map = {}
    for change, price in zip(window(diff, 4), seq[4:]):
        if change not in map:
            changes.add(change)
            map[change] = price
    num_maps.append(map)


print(
    max(sum(num_map.get(change, 0) for num_map in num_maps) for change in tqdm(changes))
)
