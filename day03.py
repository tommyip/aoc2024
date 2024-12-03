import re

line = open("inputs/day03.txt").read().strip()

matches = re.findall(r"(do|don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)", line)

part1 = 0
part2 = 0
enabled = True
for cond, a, b in matches:
    if cond:
        enabled = cond == "do"
    else:
        part1 += int(a) * int(b)
        if enabled:
            part2 += int(a) * int(b)

print(part1)
print(part2)
