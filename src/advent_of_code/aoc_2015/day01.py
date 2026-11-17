# day01.py

def part1(data: str) -> int:
    return sum(1 if c == "(" else -1 for c in data)


def part2(data: str) -> int:
    floor = 0
    for i, c in enumerate(data):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i
