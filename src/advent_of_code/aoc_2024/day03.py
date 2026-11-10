# day03.py

import re


MUL_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"
DONT_REGEX = r"(?s)don't\(\).*?do\(\)"


def calc_multiplications_in_str(data: str) -> int:
    return sum(int(a) * int(b) for (a, b) in re.findall(MUL_REGEX, data))


def part1(data: str) -> int:
    return calc_multiplications_in_str(data)


def part2(data: str) -> int:
    return calc_multiplications_in_str(re.sub(DONT_REGEX, "", data))
