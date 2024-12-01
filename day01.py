from collections import Counter

nums = [*map(int, open("inputs/day01.txt").read().strip().split())]
l, r = sorted(nums[0::2]), sorted(nums[1::2])

print(sum(abs(a - b) for a, b in zip(l, r)))

count = Counter(r)
print(sum(a * count.get(a, 0) for a in l))
