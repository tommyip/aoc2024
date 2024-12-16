from aoc_utils import *

inputs = open("inputs/day16.txt").read().strip()
grid = complex_grid(inputs.replace("E", ".").split("\n"))
start = grid_find(inputs, "S")
end = grid_find(inputs, "E")

dist = {(start, 1): (0, [])}

unvisited = set()
for pos, c in grid.items():
    if c in "S.":
        for dir in adj4:
            unvisited.add((pos, dir))

while unvisited:
    pos, cost = None, None
    for pos_ in unvisited:
        if cost_and_parent := dist.get(pos_):
            cost_, _ = cost_and_parent
            if cost is None or cost_ < cost:
                pos = pos_
                cost = cost_
    if pos is None or cost is None:
        break
    loc, dir = pos

    for nei_dir in adj4:
        if nei_dir == -dir:
            continue
        nei = loc + nei_dir
        nei_pos = nei, nei_dir
        if grid.get(nei) == "." and nei_pos in unvisited:
            nei_cost = cost + 1 + 1000 * (dir != nei_dir)
            if nei_pos in dist:
                nei_cost_, parents = dist[nei_pos]
                if nei_cost < nei_cost_:
                    dist[nei_pos] = nei_cost, [pos]
                elif nei_cost == nei_cost_:
                    parents.append(pos)
            else:
                dist[nei_pos] = nei_cost, [pos]
    unvisited.remove(pos)

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
