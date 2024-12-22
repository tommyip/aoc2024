from collections.abc import Iterable
from itertools import islice
from typing import Generic, TypeVar

inf = float("inf")
adj4 = (-1j, 1, 1j, -1)
adj8 = (-1j, 1 - 1j, 1, 1 + 1j, 1j, 1j - 1, -1, 1j - 1)
dir_map = {"^": -1j, "v": 1j, ">": 1, "<": -1}


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class CostNode(tuple, Generic[K, T]):
    cost: K
    pos: T

    def __new__(cls, cost: K, pos: T):
        self = tuple.__new__(cls, (cost, pos))
        self.cost = cost
        self.pos = pos
        return self

    def __lt__(self, other):
        return self.cost < other.cost


def complex_grid(
    input: Iterable[Iterable[T]],
    filter: Iterable[T] | None = None,
    inv: bool = False,
) -> dict[complex, T]:
    return {
        i + j * 1j: c
        for j, line in enumerate(input)
        for i, c in enumerate(line)
        if not filter or (not inv and c in filter) or c not in filter
    }


def grid_find(grid: str | list[str], target: str) -> complex:
    if isinstance(grid, str):
        grid = grid.split("\n")
    for j, line in enumerate(grid):
        for i, c in enumerate(line):
            if c == target:
                return complex(i, j)
    return complex(float("inf"), float("inf"))


def find_key_by_value(d: dict[K, V], v: V) -> K:
    return list(d.keys())[list(d.values()).index(v)]


def ij(x: complex) -> tuple[int, int]:
    return int(x.real), int(x.imag)


def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
