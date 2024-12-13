import re

from sympy import solve
from sympy.abc import a, b
from tqdm import tqdm

inputs = open("inputs/day13.txt").read().split("\n\n")


def tokens(ax, ay, bx, by, px, py, trans=0):
    sols = solve(
        [a * ax + b * bx - trans - px, a * ay + b * by - trans - py], [a, b], dict=True
    )

    for sol in sols:
        if (
            sol[a] >= 0
            and sol[a] == int(sol[a])
            and sol[b] >= 0
            and sol[b] == int(sol[b])
        ):
            return sol[a] * 3 + sol[b]
    return 0


part1 = 0
part2 = 0
for task in tqdm(inputs):
    args = list(map(int, re.findall(r"\d+", task)))
    part1 += tokens(*args)
    part2 += tokens(*args, trans=10000000000000)

print(part1)
print(part2)
