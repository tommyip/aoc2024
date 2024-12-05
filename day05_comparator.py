from collections import defaultdict

rules, updates = map(str.splitlines, open("inputs/day05.txt").read().split("\n\n"))

part = [0, 0]
order = defaultdict(set)
for line in rules:
    a, b = map(int, line.split("|"))
    order[a].add(b)


class Ordering(int):
    def __lt__(self, other):
        return self in order and other in order[self]


for update in updates:
    nums = list(map(int, update.split(",")))
    correct = sorted(nums, key=Ordering)
    part[nums == correct] += correct[len(correct) // 2]

print(part[1])
print(part[0])
