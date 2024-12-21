from functools import cache
from itertools import pairwise, product

from aoc_utils import *

inputs = open("inputs/day21.txt").read().splitlines()
num_pad = "789", "456", "123", " 0A"
dir_pad = " ^A", "<v>"
grids = {
    "num": complex_grid(num_pad, filter=" ", inv=True),
    "dir": complex_grid(dir_pad, filter=" ", inv=True),
}


@cache
def base_shortest_paths(src, dist, pad):
    grid = grids[pad]
    s = [(src, "", set())]
    paths = []
    while s:
        pos, path, visited = s.pop()
        if pos == dist:
            paths.append(path)
            continue
        visited = visited | {pos}
        for dir, key in zip(adj4, "^>v<"):
            nei = pos + dir
            if nei in grid and nei not in visited:
                s.append((nei, path + key, visited))
    min_len = min(map(len, paths))
    return [p for p in paths if len(p) == min_len]


def path_combinations(keys, pad):
    path = []
    grid = grids[pad]
    for src_key, dest_key in pairwise(keys):
        src = find_key_by_value(grid, src_key)
        dest = find_key_by_value(grid, dest_key)
        subpaths = base_shortest_paths(src, dest, pad)
        path.append(subpaths)
        path.append(["A"])
    return ("".join(l) for l in product(*path))


@cache
def shortest_path_len(code, level, pad):
    paths = path_combinations(code, pad)
    if level == 0:
        return min(map(len, paths))
    return min(
        sum(
            shortest_path_len(src + dist, level - 1, "dir")
            for src, dist in pairwise("A" + path)
        )
        for path in paths
    )


def complexity(code, level):
    min_len = shortest_path_len("A" + code, level, "num")
    return min_len * int(code[:-1])


print(sum(complexity(code, 2) for code in inputs))
print(sum(complexity(code, 25) for code in inputs))
