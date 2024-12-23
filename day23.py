from collections import defaultdict
from itertools import combinations

inputs = open("inputs/day23.txt").read().splitlines()

network = defaultdict(set)
for line in inputs:
    a, b = line.split("-")
    network[a].add(b)
    network[b].add(a)

part1 = set()
for a, neis in network.items():
    for b, c in combinations(neis, r=2):
        triple = tuple(sorted((a, b, c)))
        if (
            any(x[0] == "t" for x in triple)
            and {b, c} <= network[a]
            and {a, c} <= network[b]
            and {a, b} <= network[c]
        ):
            part1.add(triple)
print(len(part1))


part2 = None
party_size = max(map(len, network.values()))
for node in network:
    for friends in combinations(network[node], r=party_size - 1):
        party = set(friends + (node,))
        if all(party - {friend} <= network[friend] for friend in party):
            part2 = ",".join(sorted(party))
            break
    if part2:
        break
print(part2)
