from tqdm import tqdm

lines = open("inputs/day07.txt").read().splitlines()


def possible(nums, acc, expected, is2=False):
    if len(nums) == 0:
        return acc == expected
    if acc > expected:
        return False
    x = nums[0]
    return (
        possible(nums[1:], acc + x, expected, is2)
        or possible(nums[1:], acc * x, expected, is2)
        or is2
        and possible(nums[1:], int(f"{acc}{x}"), expected, is2)
    )


part1 = 0
part2 = set()
for line in tqdm(lines):
    test, start, *nums = map(int, line.replace(":", "").split(" "))
    if possible(nums, start, test):
        part1 += test
        part2.add(test)
    if possible(nums, start, test, is2=True):
        part2.add(test)


print(part1)
print(sum(part2))
