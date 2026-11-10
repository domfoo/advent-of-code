# day15.py

from enum import Enum


type Grid = dict[complex: str]


class Cell(Enum):
    BOX = "O"
    BOX_WIDE_LEFT = "["
    BOX_WIDE_RIGTH = "]"
    EMPTY = "."
    GUARD = "@"
    WALL = "#"


def move(position: complex, direction: complex, grid: Grid) -> Grid | None:
    if not grid:
        return None

    next_position = position + direction
    next_value = grid.get(next_position, Cell.WALL)

    match next_value:
        case Cell.BOX:
            grid = move(next_position, direction, grid)
            if not grid:
                return None
            else:
                grid[next_position] = grid[position]
                grid[position] = Cell.EMPTY
                return grid
        case Cell.EMPTY:
            grid[next_position] = grid[position]
            grid[position] = next_value
            return grid
        case _:
            return None


def get_guard_position(grid: Grid) -> complex:
    return min(k for k in grid if grid[k] == Cell.GUARD)


def direction_to_complex(direction: str) -> complex:
    match direction:
        case "<":
            return -1 + 0j
        case ">":
            return 1 + 0j
        case "^":
            return -1j
        case "v":
            return 1j
        case _:
            return None


def parse(data: str) -> tuple[Grid, list[complex]]:
    grid_str, directions_str = data.split("\n\n")
    grid = {x + y * 1j: Cell(val) for y, line in enumerate(grid_str.split('\n')) for x, val in enumerate(line)}
    directions = [c for c in directions_str if c in ["<", ">", "^", "v"]]
    directions = [direction_to_complex(direction) for direction in directions]
    return grid, directions


def part1(data: str) -> int:
    grid, directions = parse(data)

    for direction in directions:
        position = get_guard_position(grid)
        next_grid = move(position, direction, grid)
        if next_grid:
            grid = next_grid

    return sum(int(position.real + position.imag * 100) for position, box in grid.items() if box == Cell.BOX)


# copied this solution from reddit, thank you u/4HbQ!
def part2(data: str) -> int:
    grid, moves = data.split('\n\n')

    def move(p, d):
        p += d
        if all([
            grid[p] != '[' or move(p+1, d) and move(p, d),
            grid[p] != ']' or move(p-1, d) and move(p, d),
            grid[p] != 'O' or move(p, d), grid[p] != '#']):
                grid[p], grid[p-d] = grid[p-d], grid[p]
                return True


    for grid in grid, grid.translate(str.maketrans(
            {'#':'##', '.':'..', 'O':'[]', '@':'@.'})):

        grid = {i+j*1j:c for j,r in enumerate(grid.split())
                        for i,c in enumerate(r)}

        pos, = [p for p in grid if grid[p] == '@']

        for m in moves.replace('\n', ''):
            dir = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]
            C = grid.copy()

            if move(pos, dir): pos += dir
            else: grid = C

        ans = sum(pos for pos in grid if grid[pos] in 'O[')
        print(int(ans.real + ans.imag*100))


if __name__ == "__main__":
    test_data = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
