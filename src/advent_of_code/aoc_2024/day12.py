# day12.py

type Plots = dict[complex: str]
type Group = tuple[complex]


def calc_bulk_discount(group: Group) -> int:
    area = len(group)
    perimeter = {(position, step) for step in [1, -1, 1j, -1j] for position in group if position + step not in group}
    sides = perimeter - {(position+step*1j, step) for position, step in perimeter}
    return len(group) * len(sides)


def calc_price(group: Group) -> int:
    perimeter = {(position, step) for step in [1, -1, 1j, -1j] for position in group if position + step not in group}
    return len(group) * len(perimeter)


def find_groups(plots: Plots) -> set[Group]:    
    groups = {position: {position} for position in plots}

    for group in groups:
        for next_pos in [group + step for step in [1, -1, 1j, -1j]]:
            if plots.get(group) == plots.get(next_pos):
                groups[group] |= groups[next_pos]
                for x in groups[group]:
                    groups[x] = groups[group]

    return {tuple(group) for group in groups.values()}


def parse(data: str) -> Plots:
    return {x + y * 1j: val for y, line in enumerate(data.split('\n')) for x, val in enumerate(line)}


def part1(data: str) -> int:
    plots = parse(data)
    groups = find_groups(plots)
    return sum(calc_price(group) for group in groups)


def part2(data: str) -> int:
    plots = parse(data)
    groups = find_groups(plots)
    return sum(calc_bulk_discount(group) for group in groups)


if __name__ == "__main__":
    test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
