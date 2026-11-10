# day02.py

MIN_DISTANCE = 1
MAX_DISTANCE = 3

def all_but_one(iterable) -> bool:
    iterable = list(iterable)
    print(iterable, [1 for x in iterable if not bool(x)], sum(1 for x in iterable if not bool(x)))
    return len([1 for x in iterable if not bool(x)]) <= 1
    any(safe(report[:i]+report[i+1:]) for i in range(len(report)))


def is_allowed_absolute_values(distances: list[int]) -> bool:
    return all(abs(x) in range(MIN_DISTANCE, MAX_DISTANCE + 1) for x in distances)


def is_monotonous(distances: list[int]) -> bool:
    return all(x > 0 for x in distances) or all(x < 0 for x in distances)


def calc_distances(report: list[int]) -> list[int]:
    return [b - a for a, b in zip(report, report[1:])]


def is_safe_dampened(report: list[int]) -> bool:
    return any(is_safe(report[:i]+report[i+1:]) for i in range(len(report)))


def is_safe(report: list[int]) -> bool:
    distances = calc_distances(report)
    return is_monotonous(distances) and is_allowed_absolute_values(distances)


def get_reports(data: str) -> list[list[int]]:
    reports_str = [line.split() for line in data.split("\n")]
    return [[int(x) for x in report] for report in reports_str]


def part1(data: str) -> int:
    return len([report for report in get_reports(data) if is_safe(report)])


def part2(data: str) -> int:
    return len([report for report in get_reports(data) if is_safe_dampened(report)])
