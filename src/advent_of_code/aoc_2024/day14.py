# day14.py

from re import findall
from itertools import batched
from time import sleep

ROBOT_REGEX = r"-?\d+"

type Robot = tuple[complex, complex]


def in_quadrant(position: complex, dimension: complex) -> bool:
    if position.real in range(int(dimension.real / 2)) and position.imag in range(int(dimension.imag / 2)):
        return 1 # first quadrant
    elif position.real in range(int(dimension.real / 2) + 1, int(dimension.real) + 1) and position.imag in range(int(dimension.imag / 2)):
        return 2 # second quadrant
    elif position.real in range(int(dimension.real / 2)) and position.imag in range(int(dimension.imag / 2) + 1, int(dimension.imag) + 1):
        return 3 # second quadrant
    elif position.real in range(int(dimension.real / 2) + 1, int(dimension.real) + 1) and position.imag in range(int(dimension.imag / 2) + 1, int(dimension.imag) + 1):
        return 4 # second quadrant
    else:
        return None # no quadrant


def move_robot(robot: Robot, dimension: complex) -> Robot:
    pos = robot[0] + robot[1]
    return (complex(pos.real % dimension.real, pos.imag % dimension.imag), robot[1])


def robots_gen(robots: list[Robot], dimension: complex) -> list[Robot]:
    while True:
        yield robots
        robots = [move_robot(robot, dimension) for robot in robots]


def calc_robot_steps(start: complex, direction: complex, dimension: complex, steps: int) -> complex:
    position = start

    for _ in range(steps):
        position = position + direction
        position = complex(position.real % dimension.real, position.imag % dimension.imag)
    
    return position


def parse(data: str) -> list[Robot]:
    return [(complex(int(x[0]), int(x[1])), complex(int(x[2]), int(x[3]))) for x in batched(findall(ROBOT_REGEX, data), 4)]


def part1(data: str) -> int:
    steps = 100
    dimension = 101 + 103j
    robots = parse(data)
    destinations = [calc_robot_steps(robot[0], robot[1], dimension, steps) for robot in robots]

    quadrants = {1: [], 2: [], 3: [], 4: []}
    
    for p in destinations:
        if q:= in_quadrant(p, dimension):
            quadrants[q].append(p)

    result = 1
    for l in quadrants.values():
        result *= len(l)

    return result


def part2(data: str) -> int:
    dimension = 101 + 103j
    robots = parse(data)

    steps = 0
    for rs in robots_gen(robots, dimension):
        positions = [p for p, v in rs]
        
        # enter slow mode for better visual, I just print them and look, if there is a christmas tree, idc
        if steps > 6300:
            sleep(1/30)
            for i in range(int(dimension.imag)):
                for j in range(int(dimension.real)):
                    if complex(j, i) in positions:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print()
            
            print("Step", steps)
            print()
        steps += 1
