# day06.py

from multiprocessing import Pool


def walk(grid: dict[complex: str]) -> (set[complex], bool):
    position = min(k for k in grid if grid[k] == "^")
    direction = -1j
    visited = set()

    while position in grid and (position, direction) not in visited:
        visited.add((position, direction))
        if grid.get(position + direction) == "#":
            direction *= 1j
        else:
            position += direction

    return {p for p, _ in visited}, (position, direction) in visited


def walk_path(grid: dict[complex: str]) -> set[complex]:
    return walk(grid)[0]


def is_path_cycle(grid: dict[complex: str]) -> bool:
    return walk(grid)[1]


def get_grid(data: str) -> dict[complex: str]:
    return {x + y * 1j: val for y, line in enumerate(data.split('\n')) for x, val in enumerate(line)}


def part1(data: str) -> int:
#     data = """....#.....
# ...lar...#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

    grid = get_grid(data)
    return len(walk_path(grid))


def part2(data: str) -> int:
#     data = """....#.....
# ...lar...#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

    grid = get_grid(data)
    path = walk_path(grid)
    grids_with_obstacles = (grid | {position: "#"} for position in path if grid[position] != "^")

    with Pool() as pool:
        return sum(pool.map(is_path_cycle, grids_with_obstacles))
