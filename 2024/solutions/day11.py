# day11.py

from functools import cache


@cache
def calc_number_of_stones(stone: int, blinks: int) -> int:
    if blinks <= 0:
        return 1

    if stone == 0:
        return calc_number_of_stones(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        length = len(str(stone))
        left, right = int(str(stone)[:length//2]), int(str(stone)[length//2:])
        return calc_number_of_stones(left, blinks - 1) + calc_number_of_stones(right, blinks - 1)
    else:
        return calc_number_of_stones(stone * 2024, blinks - 1)


def solve(data: str, blinks: int) -> int:
    stones = [int(s) for s in data.split()]
    return sum(calc_number_of_stones(stone, blinks) for stone in stones)


def part1(data: str) -> int:
    blinks = 25
    return solve(data, blinks)


def part2(data: str) -> int:
    blinks = 75
    return solve(data, blinks)


if __name__ == "__main__":
    test_data = "125 17"
    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))