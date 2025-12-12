# solutions/day12.py

import numpy as np


def check_area(dim: tuple[int, int], quantities: list[int], presents: list[np.ndarray]) -> bool:
    area = sum(np.sum(presents[i]) * q for i, q in enumerate(quantities))

    return area <= dim[0] * dim[1]


def parse(data: str) -> tuple[list[np.ndarray], list[tuple[tuple[int, int], list[int]]]]:
    blocks = data.split("\n\n")

    presents = []

    for block in blocks[:-1]:
        present = []
        for line in block.splitlines()[1:]:
            present_line = []
            for c in line:
                present_line.append(1 if c == "#" else 0)
            present.append(present_line)
        presents.append(np.array(present))

    trees = []
    for line in blocks[-1].splitlines():
        dim, n = line.split(": ")
        dim = tuple(map(int, dim.split("x")))
        n = [int(x) for x in n.split()]
        trees.append((dim, n))

    return presents, trees


def part1(data: str):
    presents, trees = parse(data)
    return sum(check_area(dim, quantities, presents) for dim, quantities in trees)


def part2(data: str):
    pass


if __name__ == "__main__":
    test_data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
