from collections import defaultdict
from itertools import groupby

inputs = open("inputs/day12.txt").read().splitlines()
m = defaultdict(
    str, {i + j * 1j: c for j, line in enumerate(inputs) for i, c in enumerate(line)}
)
visited = set()
dirs = [-1j, 1, 1j, -1]


def price(pos, connected):
    visited.add(pos)
    connected.add(pos)
    plant = m[pos]
    perimeter = 4 - sum(m[pos + dir] == plant for dir in dirs)
    area = 0
    for dir in dirs:
        nei = pos + dir
        if m[nei] == plant and nei not in visited:
            p, a = price(nei, connected)
            perimeter += p
            area += a
    return perimeter, area + 1


def discount_perimeter(connected):
    min_w = min(int(x.real) for x in connected)
    min_h = min(int(x.imag) for x in connected)
    w = max(int(x.real) for x in connected) - min_w + 1
    h = max(int(x.imag) for x in connected) - min_h + 1
    region = [[False] * w for _ in range(h)]
    for pos in connected:
        region[int(pos.imag) - min_h][int(pos.real) - min_w] = True
    sides = 0
    for k in range(4):
        if k != 0:
            # Rotate region 90deg
            region = list(zip(*region[::-1]))
        # Find number of connected sides for the top edge
        for j, line in enumerate(region):
            prev_line = region[j - 1] if j > 0 else [False] * len(region[0])
            is_side = [a and not b for a, b in zip(line, prev_line)]
            sides += sum(g for g, _ in groupby(is_side))
    return sides


part1 = 0
part2 = 0
for pos in list(m):
    if pos not in visited:
        connected = set()
        perim, area = price(pos, connected)
        discount_perim = discount_perimeter(connected)
        part1 += area * perim
        part2 += area * discount_perim

print(part1)
print(part2)
