from collections import defaultdict
from itertools import combinations

inputs = open("inputs/day23.txt").read().splitlines()
network = defaultdict(set)
for line in inputs:
    a, b = line.split("-")
    network[a].add(b)
    network[b].add(a)


def parties(size):
    for node in network:
        for friends in combinations(network[node], r=size - 1):
            party = set(friends + (node,))
            if all(party - {friend} <= network[friend] for friend in party):
                yield ",".join(sorted(party))


print(sum("t" in p[::3] for p in set(parties(3))))
print(next(parties(len(network[a]))))
