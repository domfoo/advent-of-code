# day18.py

from re import findall
from enum import Enum
from collections import deque


START = 0+0j
END = 6+6j


class Cell(Enum):
    EMPTY = "."
    CORRUPT = "#"
    PATH = "O"


def floodfill(space, position):
    cell = space.get(position)
    if cell == Cell.EMPTY:
        space[position] = Cell.PATH

        if space.get(position + 1):
            floodfill(space, position + 1)
        if space.get(position - 1):
            floodfill(space, position - 1)
        if space.get(position + 1j):
            floodfill(space, position + 1j)
        if space.get(position - 1j):
            floodfill(space, position - 1j)


def find_shortest_path(space: dict[complex], start: complex, end: complex):
    q = deque()
    q.append(start)
    visited = {start}

    while q:
        pos = q.popleft()

        if pos == end:
            return

        if pos not in visited:
            visited.add(pos)

        if space.get(pos + 1) and space.get(pos + 1) == Cell.EMPTY:
            q.append(pos + 1)
        if space.get(pos - 1) and space.get(pos - 1) == Cell.EMPTY:
            q.append(pos - 1)
        if space.get(pos + 1j) and space.get(pos + 1j) == Cell.EMPTY:
            q.append(pos + 1j)
        if space.get(pos - 1j) and space.get(pos - 1j) == Cell.EMPTY:
            q.append(pos - 1j)


def print_space(space: dict[complex]):
    for y in range(int(END.imag) + 1):
        for x in range(int(END.real) + 1):
            print(space.get(complex(x, y)).value, end="")
        print()


def parse(data: str) -> list[complex]:
    return [complex(int(x), int(y)) for x, y in findall(r"(\d+),(\d+)", data)]


def part1(data: str) -> str:
    space = {complex(x, y): Cell.EMPTY for x in range(int(END.real) + 1) for y in range(int(END.imag) + 1)}
    coords = parse(data)

    for i in range(12):
        space[coords[i]] = Cell.CORRUPT
    print_space(space)
    print()

    # floodfill(space, START)
    q = find_shortest_path(space, START, END)
    print_space(space)

    return q


def part2(data: str) -> str:
    pass


if __name__ == "__main__":
    test_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
