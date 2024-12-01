# day01.py

from collections import Counter


def get_sorted_lists_from_data(data: str) -> (list[int], list[int]):
    numbers = [int(x) for x in data.split()]
    return (sorted(numbers[::2]), sorted(numbers[1::2]))


def part1(data: str) -> int:
    left_list, right_list = get_sorted_lists_from_data(data)
    return sum([abs(b - a) for a, b in zip(left_list, right_list)])


def part2(data: str) -> int:
    left_list, right_list = get_sorted_lists_from_data(data)
    counter = Counter(right_list)
    return sum([number * counter.get(number, 0) for number in left_list])