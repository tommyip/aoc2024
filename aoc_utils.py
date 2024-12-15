from collections.abc import Iterable
from typing import TypeVar

adj4 = (-1j, 1, 1j, -1)
adj8 = (-1j, 1 - 1j, 1, 1 + 1j, 1j, 1j - 1, -1, 1j - 1)
dir_map = {"^": -1j, "v": 1j, ">": 1, "<": -1}


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def complex_grid(
    input: Iterable[Iterable[T]], filter: Iterable[T] | None = None
) -> dict[complex, T]:
    return {
        i + j * 1j: c
        for j, line in enumerate(input)
        for i, c in enumerate(line)
        if not filter or c in filter
    }


def grid_find(grid: str, target: str) -> complex:
    for j, line in enumerate(grid.split("\n")):
        for i, c in enumerate(line):
            if c == target:
                return complex(i, j)
    return complex(float("inf"), float("inf"))


def find_key_by_value(d: dict[K, V], v: V) -> K:
    return list(d.keys())[list(d.values()).index(v)]