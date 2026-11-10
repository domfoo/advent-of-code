# day08.py

from itertools import takewhile


def antinode_gen(start: complex, step: complex):
    i = 0
    while True:
        yield start + step * i
        i += 1


def get_antennas(grid: dict[complex: str]) -> dict[str, list[complex]]:
    antennas = {}
    for k, v in grid.items():
        if v != ".":
            antennas[v] = antennas.get(v, []) + [k]
    return antennas


def parse(data: str) -> dict[complex: str]:
    return {x + y * 1j: val for y, line in enumerate(data.split('\n')) for x, val in enumerate(line)}


def part1(data: str) -> int:
#     data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

    grid = parse(data)
    antennas = get_antennas(grid)
    antinodes = set()

    for positions in antennas.values():
        pairs = ((a, b) for a in positions for b in positions if a != b)

        for a, b in pairs:
            step = b - a
            antinodes |= {b + step, a - step}

    return len([antinode for antinode in antinodes if antinode in grid])


def part2(data: str) -> int:
#     data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

    grid = parse(data)
    antennas = get_antennas(grid)
    antinodes = set()

    for positions in antennas.values():
        pairs = ((a, b) for a in positions for b in positions if a != b)

        for a, b in pairs:
            step = b - a
            antinodes.update(takewhile(lambda n: n in grid, antinode_gen(b, step)))
            antinodes.update(takewhile(lambda n: n in grid, antinode_gen(a, -step)))


    return len(antinodes)
