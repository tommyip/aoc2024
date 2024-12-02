from itertools import pairwise

lines = open("inputs/day02.txt").read().splitlines()


def safe(levels):
    sl = sorted(levels)
    if levels == sl or levels == sl[::-1]:
        return all([1 <= abs(x - y) <= 3 for x, y in pairwise(levels)])
    return False


part1 = 0
part2 = 0
for line in lines:
    levels = [int(x) for x in line.split()]
    if safe(levels):
        part1 += 1
        part2 += 1
        continue
    for i in range(len(levels)):
        if safe([x for j, x in enumerate(levels) if i != j]):
            part2 += 1
            break

print(part1)
print(part2)
