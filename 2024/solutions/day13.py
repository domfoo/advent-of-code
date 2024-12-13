# day13.py

from re import findall
import numpy as np


MACHINE_REGEX = r"Button A: X\+(\d+), Y\+(\d+)\WButton B: X\+(\d+), Y\+(\d+)\WPrize: X=(\d+), Y=(\d+)"


def parse(data: str) -> list[tuple[np.array, np.array]]:
    tmp = [[int(x) for x in m] for m in findall(MACHINE_REGEX, data)]
    return [(np.transpose([m[:2], m[2:4]]), np.array(m[4:])) for m in tmp]


def part1(data: str) -> int:
    results = []
    for M, P in parse(data):
        R = np.linalg.solve(M, P).round().astype(int)
        if all(M @ R == P):
            results.append(R)

    return sum(3 * result[0] + result[1] for result in results)


def part2(data: str) -> int:
    results = []
    for M, P in parse(data):
        P = P + 10000000000000
        R = np.linalg.solve(M, P).round().astype(int)
        if all(M @ R == P):
            results.append(R)

    return sum(3 * result[0] + result[1] for result in results)


if __name__ == "__main__":
    test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
