from aoc_utils import *

grid, moves = open("inputs/day15.txt").read().split("\n\n")
moves = moves.replace("\n", "")


def part1(grid, moves):
    grid = grid.split("\n")
    pos = grid_find(grid, "@")
    grid = complex_grid(grid, filter="#O")

    for move in moves:
        dir = dir_map[move]
        pos_, start, end = pos, 0, 0
        while True:
            pos_ += dir
            if pos_ not in grid:
                pos += dir
                if start:
                    del grid[start]
                    grid[end + dir] = "O"
                break
            elif grid[pos_] == "O":
                if not start:
                    start = pos_
                end = pos_
            elif grid[pos_] == "#":
                break
    return grid


def part2(grid, moves):
    grid = grid.translate(
        str.maketrans({"#": "##", "O": "[]", ".": "..", "@": "@."})
    ).split("\n")
    pos = grid_find(grid, "@")
    grid = complex_grid(grid, filter="#[]")

    for move in moves:
        dir = dir_map[move]
        boxes = {}
        pos_ = pos + dir
        if pos_ not in grid:
            pos = pos_
        elif grid.get(pos_, ".") in "[]":
            # Find connected components (boxes)
            change = True
            if dir.real:  # Move horizontal
                while True:
                    match grid.get(pos_, None):
                        case None:
                            break
                        case "[" | "]":
                            boxes[pos_] = grid[pos_]
                            pos_ += dir
                        case "#":
                            change = False
                            break
            else:  # Move Vertical
                if grid[pos_] == "]":
                    pos_ = pos_ - 1
                boxes[pos_] = "["
                boxes[pos_ + 1] = "]"
                front = {pos_}
                while change:
                    front_ = set()
                    for pos_ in front:
                        if (
                            grid.get(pos_ + dir) == "#"
                            or grid.get(pos_ + 1 + dir) == "#"
                        ):
                            change = False
                            break
                        elif grid.get(pos_ + dir) == "[":
                            boxes[pos_ + dir] = "["
                            boxes[pos_ + dir + 1] = "]"
                            front_.add(pos_ + dir)
                        else:
                            if grid.get(pos_ + dir) == "]":
                                boxes[pos_ + dir] = "]"
                                boxes[pos_ + dir - 1] = "["
                                front_.add(pos_ + dir - 1)
                            if grid.get(pos_ + dir + 1) == "[":
                                boxes[pos_ + dir + 1] = "["
                                boxes[pos_ + dir + 2] = "]"
                                front_.add(pos_ + dir + 1)

                    if front_:
                        front = front_
                    else:
                        break
            if change:
                pos += dir
                for p in boxes:
                    del grid[p]
                for p, item in boxes.items():
                    grid[p + dir] = item
    return grid


def coords_sum(grid):
    return int(sum(pos.imag * 100 + pos.real for pos, c in grid.items() if c in "O["))


print(coords_sum(part1(grid, moves)))
print(coords_sum(part2(grid, moves)))
