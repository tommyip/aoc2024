from graphlib import TopologicalSorter

from aoc_utils import *

l, r = open("inputs/day24.txt").read().strip().split("\n\n")

values, logic, g = {}, {}, {}
for line in l.split("\n"):
    zx, value = line.split(": ")
    values[zx] = int(value)
for line in r.split("\n"):
    a, op, b, _, out = line.split(" ")
    logic[out] = op, a, b
    g[out] = {a, b}

topo = [(x, logic[x]) for x in TopologicalSorter(g).static_order() if x not in values]
for gate, (op, a, b) in topo:
    match op:
        case "AND":
            values[gate] = values[a] and values[b]
        case "OR":
            values[gate] = values[a] or values[b]
        case "XOR":
            values[gate] = values[a] ^ values[b]

bitsmap = {k: str(v) for k, v in values.items() if "z" in k}
print(int("".join(bitsmap[z] for z in reversed(sorted(bitsmap))), 2))


wrong = set()
for i in range(1, 45):
    zi = f"z{i:02}"
    z_op, *_ = logic[zi]
    if z_op != "XOR":
        wrong.add(zi)
    aibi = [f"x{i:02}", f"y{i:02}"]
    axb = find_key_by_predicate(
        logic, lambda tup: tup[0] == "XOR" and sorted(tup[1:]) == aibi
    )
    z = find_key_by_predicate(logic, lambda tup: tup[0] == "XOR" and axb in tup[1:])
    cab = find_key_by_predicate(logic, lambda tup: tup[0] == "AND" and axb in tup[1:])
    if z is None or cab is None:
        wrong.add(axb)
    elif z != zi:
        wrong.add(z)
    ab = find_key_by_predicate(
        logic, lambda tup: tup[0] == "AND" and sorted(tup[1:]) == aibi
    )
    if not find_key_by_predicate(logic, lambda tup: tup[0] == "OR" and ab in tup[1:]):
        wrong.add(ab)
print(",".join(sorted(wrong)))
