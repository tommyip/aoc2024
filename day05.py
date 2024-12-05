from collections import defaultdict

rules, updates = map(str.splitlines, open("inputs/day05.txt").read().split("\n\n"))

part1 = 0
part2 = 0
order = defaultdict(set)
for line in rules:
    a, b = map(int, line.split("|"))
    order[a].add(b)

for update in updates:
    nums = list(map(int, update.split(",")))
    wrong = False
    for i, num in enumerate(nums):
        if num not in order:
            continue
        before = nums[:i]
        later = order[num]
        if any(x in before for x in later):
            wrong = True
            break
    else:
        part1 += nums[len(nums) // 2]

    if wrong:
        ordered = []
        remaining = set(nums)
        while remaining:
            for num in remaining:
                if num not in order or order[num].isdisjoint(remaining):
                    remaining.remove(num)
                    ordered.append(num)
                    break
        part2 += ordered[len(nums) // 2]

print(part1)
print(part2)
