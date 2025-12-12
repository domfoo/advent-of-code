# solutions/day10.py

from itertools import product
from functools import reduce
from operator import xor, add


def add_lists(l1: list[int], l2: list[int]) -> list[int]:
    return [a + b for a, b in zip(l1, l2)]


def solve_ilp(objective, target, domains):
    candidates = []

    for x in product(*domains):
        if objective(x) == target:
            candidates.append(x)
    
    if not candidates:
        return None

    return min(candidates, key=sum)


def parse(data: str) -> list[tuple[int, list[int], list[int]]]:
    for line in data.splitlines():
        elems = line.split()
        a = int(elems[0][1:-1].replace(".", "0").replace("#", "1"), 2)
        
        nums = [[int(n) for n in elem[1:-1].split(",")] for elem in elems[1:-1]]
        b = [int("".join(["1" if i in n else "0" for i in range(len(elems[0][1:-1]))]), 2) for n in nums]
        b_list = [[1 if i in n else 0 for i in range(len(elems[0][1:-1]))] for n in nums]

        c = [int(n) for n in elems[-1][1:-1].split(",")]
        yield a, b, b_list, c


def part1(data: str):
    res = 0
    for a, b, _, _ in parse(data):
        objective = lambda x: reduce(xor, (bi * xi for bi, xi in zip(b, x)))
        domains = [range(2) for _ in b]
        res += sum(solve_ilp(objective, a, domains))

    return res


# should actually find a soltion for real input, but is way to slow because of brute force
def part2(data: str):
    res = 0
    for _, b, b_list, c in parse(data):
        objective = lambda x: reduce(add_lists, ([bij * xi for bij in bi] for bi, xi in zip(b_list, x)))
        domains = [range(max(c)+1) for _ in b_list]
        res += sum(solve_ilp(objective, c, domains))

    return res


if __name__ == "__main__":
    test_data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
