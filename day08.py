from collections import defaultdict
from itertools import permutations

input = open("inputs/day08.txt").read().splitlines()
m = {complex(i, j): c for j, line in enumerate(input) for i, c in enumerate(line)}
ants = defaultdict(list)
for pos, ant in m.items():
    if ant != ".":
        ants[ant].append(pos)

part1 = set()
part2 = set()
for ant, pos_list in ants.items():
    for a, b in permutations(pos_list, 2):
        dir = b - a
        target = a + dir * 2
        if target in m and m[target] != ant:
            part1.add(target)
        while a in m:
            part2.add(a)
            a += dir
print(len(part1))
print(len(part2))
