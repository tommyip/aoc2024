from collections import defaultdict

m = open("inputs/day04.txt").read().splitlines()
m = defaultdict(
    str,
    {complex(i, j): c for j, line in enumerate(m) for i, c in enumerate(line)},
)


part1 = 0
part2 = 0
for p in list(m):
    for d in (1, 1 + 1j, 1j, 1j - 1, -1, -1 - 1j, -1j, 1 - 1j):
        part1 += all(m[p + d * k] == w for k, w in enumerate("XMAS"))
    diag1 = m[p - 1 - 1j] + m[p] + m[p + 1 + 1j]
    diag2 = m[p - 1 + 1j] + m[p + 1 - 1j]
    part2 += (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MS" or diag2 == "SM")

print(part1)
print(part2)
