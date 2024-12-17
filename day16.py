from heapq import heappop, heappush
from typing import NamedTuple

from aoc_utils import *

inputs = open("inputs/day16.txt").read().strip()
grid = complex_grid(inputs.replace("E", ".").split("\n"))
start = grid_find(inputs, "S")
end = grid_find(inputs, "E")


class CostNode(NamedTuple):
    cost: int
    node: tuple[complex, complex]

    def __lt__(self, other):
        return self.cost < other.cost


dist = {(start, 1): (0, [])}
visited = set()
q = [CostNode(0, (start, 1))]

while q:
    cost, pos = heappop(q)
    if pos in visited:
        continue
    loc, dir = pos

    for nei_dir in adj4:
        if nei_dir == -dir:
            continue
        nei = loc + nei_dir
        nei_pos = nei, nei_dir
        if grid.get(nei) == "." and nei_pos not in visited:
            nei_cost = cost + 1 + 1000 * (dir != nei_dir)
            if nei_pos in dist:
                nei_cost_, parents = dist[nei_pos]
                if nei_cost < nei_cost_:
                    dist[nei_pos] = nei_cost, [pos]
                    heappush(q, CostNode(nei_cost, nei_pos))
                elif nei_cost == nei_cost_:
                    parents.append(pos)
                    heappush(q, CostNode(nei_cost, nei_pos))
            else:
                dist[nei_pos] = nei_cost, [pos]
                heappush(q, CostNode(nei_cost, nei_pos))
    visited.add(pos)

min_pos, min_cost = None, None
for (pos, dir), (cost, parents) in dist.items():
    if pos == end:
        if min_cost is None or cost < min_cost:
            min_pos = (pos, dir)
            min_cost = cost

print(min_cost)

tiles = set()


def dfs(pos):
    loc, _dir = pos
    tiles.add(loc)
    _cost, parents = dist[pos]
    for parent in parents:
        dfs(parent)


dfs(min_pos)
print(len(tiles))
