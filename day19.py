from functools import cache

patterns, designs = open("inputs/day19.txt").read().strip().split("\n\n")
patterns = set(patterns.split(", "))
designs = designs.split("\n")


@cache
def ways(design):
    if not design:
        return 1
    total = 0
    for i in range(1, len(design) + 1):
        if design[:i] in patterns:
            total += ways(design[i:])
    return total


wayss = [ways(x) for x in designs]
print(sum(w > 0 for w in wayss))
print(sum(wayss))
