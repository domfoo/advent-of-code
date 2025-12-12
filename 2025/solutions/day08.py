# solutions/day08.py

from collections import defaultdict
from itertools import combinations
from functools import reduce
from operator import mul
from pprint import pprint

def squared_distance(pair: tuple[tuple[int, int, int], tuple[int, int, int]]) -> int:
    a, b = pair[0], pair[1]
    return (b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2


def parse(data: str) -> list[tuple[int, int, int]]:
    return [tuple(map(int, line.split(","))) for line in data.splitlines()]


def part1(data: str):
    points = parse(data)

    shortest_pairs = sorted(combinations(points, 2), key=squared_distance)

    groups = [{p} for p in points]
    for item in shortest_pairs[:1000]:
        tmp = []
        for group in groups:
            if not group.isdisjoint(item):
                item = group.union(item)
            else:
                tmp.append(group)
        tmp.append(item)
        groups = tmp

    lenghts = [len(s) for s in sorted(groups, key=len, reverse=True)[:3]]
    return reduce(mul, lenghts)


def part2(data: str):
    points = parse(data)

    shortest_pairs = sorted(combinations(points, 2), key=squared_distance)

    groups = [{p} for p in points]
    for pair in shortest_pairs:
        item = pair
        tmp = []
        for group in groups:
            if not group.isdisjoint(item):
                item = group.union(item)
            else:
                tmp.append(group)
        tmp.append(item)
        groups = tmp
        if len(groups) == 1:
            return reduce(mul, [x for x, _, _ in pair])


if __name__ == "__main__":
    test_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
