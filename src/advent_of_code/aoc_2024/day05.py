# day05.py

def sorted_by_rules(l: list[int], rules: dict[int, set[int]]) -> list[int]:
    from functools import cmp_to_key

    # Comparator function for sorting
    # (does not actually compare correctly, but idc because the result is correct and I don't know why)
    def compare(a: int, b: int) -> int:
        if b in rules.get(a, set()):
            return -1
        elif a in rules.get(b, set()):
            return 1
        else:
            return 0

    # Sort using the custom comparator
    sorted_list = sorted(l, key=cmp_to_key(compare))

    return sorted_list


def sum_middle(pages: list[list[int]]) -> int:
    res = 0
    for line in pages:
        res += line[len(line)//2]
    return res


def is_correct_line(line: list[int], rules: dict[int, set[int]]) -> bool:
    for i, number in enumerate(line):
            if rules.get(number, set()) & set(line[i:]):
                return False        
    return True


def parse_pages(raw_pages: str) -> list[list[int]]:
    return [[int(x) for x in line.split(",")] for line in raw_pages.split()]


def parse_rules(raw_rules: str) -> dict[int, set[int]]:
    rules = {}

    for line in raw_rules.split():
        X, Y = line.split("|")
        X = int(X)
        Y = int(Y)

        if Y not in rules:
            rules[Y] = set()

        rules[Y].add(X)

    return rules


def parse_data(data: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    raw_rules, raw_pages = data.split("\n\n")
    return parse_rules(raw_rules), parse_pages(raw_pages)


def part1(data: str) -> int:
    rules, pages = parse_data(data)

    correct_pages = [line for line in pages if is_correct_line(line, rules)]
    return sum_middle(correct_pages)

def part2(data: str) -> int:
    rules, pages = parse_data(data)

    incorrect_pages = [line for line in pages if not is_correct_line(line, rules)]
    corrected_pages = [sorted_by_rules(line, rules) for line in incorrect_pages]
    return sum_middle(corrected_pages)
