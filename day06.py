from tqdm import tqdm

input = open("inputs/day06.txt").read().splitlines()
m = {complex(i, j): c for j, line in enumerate(input) for i, c in enumerate(line)}
start_pos = list(m.keys())[list(m.values()).index("^")]


def search():
    pos = start_pos
    dir = -1j
    visited = set()
    while (pos, dir) not in visited:
        visited.add((pos, dir))
        if pos + dir not in m:
            return False, {p for p, _ in visited}
        elif m[pos + dir] == "#":
            dir *= 1j
        else:
            pos += dir
    return True, set()


_, path = search()
print(len(path))

part2 = 0
for p in tqdm(path - {start_pos}):
    m[p] = "#"
    part2 += search()[0]
    m[p] = "."

print(part2)
