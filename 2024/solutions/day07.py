# day07.py

from operator import add, mul
from functools import reduce
from re import findall


def cat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def apply_operators(operators):
    def apply(operands: list[int], y: int):
        return [operator(x, y) for x in operands for operator in operators]

    return apply


def parse(data: str) -> list[int]:
    return [[int(x) for x in findall(r"\d+", line)] for line in data.split("\n")]


def solve(data: str, operators) -> int:
    return sum(solution for solution, x, *operands in parse(data) if solution in reduce(apply_operators(operators), operands, [x]))


def part1(data: str) -> int:
#     data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

    operators = [add, mul]
    return solve(data, operators)

def part2(data: str) -> int:
#     data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

    operators = [add, mul, cat]
    return solve(data, operators)
