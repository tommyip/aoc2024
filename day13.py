import re

inputs = open("inputs/day13.txt").read().split("\n\n")


def tokens(ax, ay, bx, by, px, py, trans=0):
    b = ((trans + py) * ax - (trans + px) * ay) / (by * ax - bx * ay)
    a = ((trans + px) - b * bx) / ax
    return int(a * 3 + b) if a.is_integer() and b.is_integer() else 0


part1 = 0
part2 = 0
for task in inputs:
    args = list(map(int, re.findall(r"\d+", task)))
    part1 += tokens(*args)
    part2 += tokens(*args, trans=10000000000000)

print(part1)
print(part2)
