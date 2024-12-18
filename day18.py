from heapq import heappop, heappush

from aoc_utils import *

inputs = open("inputs/day18.txt").read().splitlines()

W = 70
start, end = 0, W + W * 1j
bytes = [complex(*map(int, line.split(","))) for line in inputs]
grid = {i + j * 1j: "." for j in range(W + 1) for i in range(W + 1)}
for pos in bytes[:1024]:
    del grid[pos]


def dikjstra(grid):
    dist = {0j: 0}
    visited = set()
    q = [CostNode(0, 0j)]

    while q:
        cost, pos = heappop(q)
        if pos in visited:
            continue

        nei_cost = cost + 1
        for nei_dir in adj4:
            nei = pos + nei_dir
            if grid.get(nei) == "." and nei not in visited:
                if nei_cost < dist.get(nei, float("inf")):
                    dist[nei] = nei_cost
                    heappush(q, CostNode(nei_cost, nei))
        if pos == end:
            return dist[end]
        visited.add(pos)


dikjstra(grid)

for pos in bytes[1024:]:
    del grid[pos]
    if dikjstra(grid) is None:
        print(f"{int(pos.real)},{int(pos.imag)}")
        break
