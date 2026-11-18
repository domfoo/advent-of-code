# day03.py

DIRECTIONS = {
    "^": -1j,
    ">": 1+0j,
    "v": 1j,
    "<": -1+0j,
}


def part1(data: str) -> int:
    steps = [DIRECTIONS.get(c) for c in data]

    position = 0+0j
    visited = {position}

    for step in steps:
        position += step
        visited.add(position)

    return len(visited)


def part2(data: str) -> int:
    steps = [DIRECTIONS.get(c) for c in data]

    santa_position = 0+0j
    robot_position = 0+0j
    visited = {santa_position}

    for i, step in enumerate(steps):
        if i % 2 == 0:
            santa_position += step
            visited.add(santa_position)
        else:
            robot_position += step
            visited.add(robot_position)

    return len(visited)
