from heapq import heappop, heappush

from aoc_utils import *

inputs = open("inputs/day18.txt").read().splitlines()

W = 70
start, end = 0, W + W * 1j
bytes = [complex(*map(int, line.split(","))) for line in inputs]
grid = {i + j * 1j for j in range(W + 1) for i in range(W + 1)}


def steps(n):
    reachable = grid - set(bytes[: n + 1])
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
            if nei in reachable and nei not in visited:
                if nei_cost < dist.get(nei, float("inf")):
                    dist[nei] = nei_cost
                    heappush(q, CostNode(nei_cost, nei))
        if pos == end:
            return dist[end]
        visited.add(pos)


print(steps(1024))

lo, hi = 0, len(bytes)
while lo <= hi:
    mid = (lo + hi) // 2
    if steps(mid) is None:
        hi = mid - 1
    else:
        lo = mid + 1

pos = bytes[lo]
print(f"{int(pos.real)},{int(pos.imag)}")
