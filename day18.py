from bisect import bisect_left
from collections import deque

from aoc_utils import *

inputs = open("inputs/day18.txt").read().splitlines()
bytes = [complex(*map(int, line.split(","))) for line in inputs]
grid = {i + j * 1j for j in range(71) for i in range(71)}


def steps(n):
    reachable = grid - set(bytes[: n + 1]) - {0j}
    q = deque([(0j, 0)])
    while q:
        pos, dist = q.popleft()
        if pos == 70 + 70j:
            return dist
        for nei_dir in adj4:
            nei = pos + nei_dir
            if nei in reachable:
                q.append((nei, dist + 1))
                reachable.remove(nei)
    return inf


print(steps(1024))

i, j = ij(bytes[bisect_left(range(len(bytes)), inf, key=steps)])
print(f"{i},{j}")
