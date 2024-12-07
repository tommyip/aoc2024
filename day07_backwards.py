lines = open("inputs/day07.txt").read().splitlines()


def equation(nums, acc, is2=False):
    if acc < 0 or acc != int(acc):
        return False
    (*rest, num), acc = nums, int(acc)
    if not rest:
        return num == acc
    return (
        equation(rest, acc - num, is2)
        or equation(rest, acc / num, is2)
        or is2
        and str(acc).endswith(str(num))
        and equation(rest, int("0" + str(acc).removesuffix(str(num))), is2)
    )


part1 = 0
part2 = 0
for line in lines:
    test, *nums = map(int, line.replace(":", "").split(" "))
    if equation(nums, test):
        part1 += test
    elif equation(nums, test, is2=True):
        part2 += test


print(part1)
print(part1 + part2)
