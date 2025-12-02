# solutions/day02.py

from collections.abc import Iterable
from collections import deque
from itertools import chain


def parse(data: str) -> Iterable[int]:
    pairs = (pair.split("-") for pair in data.split(","))
    return chain(*(range(int(min), int(max)+1) for min, max in pairs))


def part1(data: str):
    invalid_id_sum = 0

    candidates = parse(data)

    for n in candidates:
        n_str = str(n)
        # filter out odd numbers
        if len(n_str) % 2 != 0:
            continue

        a, b = n_str[:len(n_str)//2], n_str[len(n_str)//2:]
        if a == b:
            invalid_id_sum += n

    return invalid_id_sum


def part2(data: str):
    invalid_id_sum = 0

    candidates = parse(data)

    for n in candidates:
        s = deque(str(n))
        s_rot = deque(str(n))
        for _ in range(len(s)-1):
            s_rot.rotate(1)
            if s == s_rot:
                invalid_id_sum += n
                break        

    return invalid_id_sum


if __name__ == "__main__":
    test_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
