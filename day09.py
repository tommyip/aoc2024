line = open("inputs/day09.txt").read().strip() + "0"
disk = [(i // 2, *map(int, line[i : i + 2])) for i in range(0, len(line), 2)]


def checksum(disk):
    i = 0
    x = 0
    for id, size, space in disk:
        x += sum(j * id for j in range(i, i + size))
        i += size + space
    return x


def part1(disk):
    free_i = 0
    while free_i < len(disk) - 1:
        free_id, free_size, free_space = disk[free_i]
        if free_space == 0:
            free_i += 1
            continue
        id, size, _ = disk.pop()
        disk[free_i] = free_id, free_size, 0
        disk.insert(free_i + 1, (id, min(size, free_space), max(free_space - size, 0)))
        if free_space < size:
            disk.append((id, size - free_space, 0))
        free_i += 1
    return disk


def part2(disk):
    i = len(disk) - 1
    for id in reversed(range(len(disk))):
        while disk[i][0] != id:
            i -= 1
        _, size, space = disk[i]
        for free_i, (free_id, free_size, free_space) in enumerate(disk[:i]):
            if free_space >= size:
                left_id, left_size, left_space = disk[i - 1]
                disk[i - 1] = left_id, left_size, left_space + size + space
                disk.pop(i)
                _, _, free_space = disk[free_i]
                disk[free_i] = free_id, free_size, 0
                disk.insert(free_i + 1, (id, size, free_space - size))
                break
    return disk


print(checksum(part1(disk.copy())))
print(checksum(part2(disk)))
