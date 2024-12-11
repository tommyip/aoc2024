from collections import Counter

counts = Counter(list(map(int, open("inputs/day11.txt").read().split())))


def stones(counts, n):
    for _ in range(n):
        next_counts = Counter()
        for stone, n in counts.items():
            if stone == 0:
                next_counts[1] += n
                continue
            s = str(stone)
            if len(s) % 2 == 0:
                next_counts[int(s[: len(s) // 2])] += n
                next_counts[int(s[len(s) // 2 :])] += n
                continue
            next_counts[stone * 2024] += n
        counts = next_counts
    return sum(counts.values())


print(stones(counts, 25))
print(stones(counts, 75))
