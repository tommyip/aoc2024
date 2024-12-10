lines = open("inputs/day10.txt").read().splitlines()

m = {i + j * 1j: int(h) for j, line in enumerate(lines) for i, h in enumerate(line)}


def score(pos, h):
    if m[pos] == 9:
        return {pos}, 1
    p1, p2 = set(), 0
    for dir in (-1j, 1, 1j, -1):
        nei = pos + dir
        if nei in m and m[nei] == h + 1:
            p1_, p2_ = score(nei, h + 1)
            p1.update(p1_)
            p2 += p2_
    return p1, p2


part1, part2 = 0, 0
for pos, h in m.items():
    if h == 0:
        p1, p2 = score(pos, 0)
        part1 += len(p1)
        part2 += p2


print(part1)
print(part2)
