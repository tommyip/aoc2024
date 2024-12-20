from itertools import count

from aoc_utils import *

inputs = open("inputs/day20.txt").read()
grid = set(complex_grid(inputs.splitlines(), filter="SE."))
start = grid_find(inputs, "S")
end = grid_find(inputs, "E")

pos = start
dists = {start: 0}
for dist in count(1):
    for dir in adj4:
        nei = pos + dir
        if nei in grid and nei not in dists:
            dists[nei], pos = dist, nei
            break
    if pos == end:
        break


def cheats(picosecs):
    total = 0
    signs = [(1, 1j), (-1, 1j), (1, -1j), (-1, -1j)]
    dirs = set()
    for saved in range(2, picosecs + 1):
        for i in range(0, saved + 1):
            for di, dj in signs:
                dirs.add((i * di + (saved - i) * dj, saved))

    for pos, dist in dists.items():
        for dir, saved in dirs:
            nei = pos + dir
            if nei in grid:
                if dists[nei] - dist - saved >= 100:
                    total += 1
    return total


print(cheats(2))
print(cheats(20))
