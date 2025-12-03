# solutions/day03.py

import time


def benchmark(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fn.__name__}: {end - start:.6f}s")
        return result
    return wrapper


def parse(data: str) -> list[list[int]]:
    return [[int(num) for num in line] for line in data.splitlines()]


@benchmark
def part1(data: str) -> int:
    total_joltage = 0
    banks = parse(data)

    for bank in banks:
        first = max(bank)
        i = bank.index(first)
        if i == len(bank) - 1:
            second = first
            first = max(bank[:i])
        else:
            second = max(bank[i+1:])

        joltage = int(str(first) + str(second))
        total_joltage += joltage

    return total_joltage


def find_n_highest(bank: list[int], count: int) -> list[int]:
    if count <= 0:
        return []

    for num in reversed(range(1, 10)):
        if num not in bank:
            continue
        i = bank.index(num)
        if count == len(bank[i:]):
            return bank[i:i+count]
        elif count < len(bank[i:]):
            return [num] + find_n_highest(bank[i+1:], count-1)


@benchmark
def part2(data: str) -> int:
    total_joltage = 0
    count = 12
    banks = parse(data)

    for bank in banks:
        batteries = find_n_highest(bank, count)
        joltage = int("".join(map(str, batteries)))
        total_joltage += joltage

    return total_joltage


if __name__ == "__main__":
    test_data = """987654321111111
811111111111119
234234234234278
818181911112111
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
