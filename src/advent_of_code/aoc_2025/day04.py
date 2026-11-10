# day05.py

def remove_paper_rolls(input: dict[complex, str]) -> int:
    res = 0

    steps = [1+0j, 1+1j, 0+1j, -1+1j, -1+0j, -1-1j, 0-1j, 1-1j]
    step_count = 0
    to_be_removed = []

    for key, val in input.items():
        if val != ".":
            step_count = 0
            for step in steps:
                neighbor = input.get(key+step)
                if neighbor and neighbor != ".":
                    step_count += 1
            if step_count < 4:
                res += 1
                to_be_removed.append(key)

    for key in to_be_removed:
        input[key] = "."

    return res, input


def parse(data: str) -> dict[complex, str]:
    res = {}
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            res[complex(int(x), int(y))] = c
    return res

def part1(data: str) -> int:
    input = parse(data)
    res, _ = remove_paper_rolls(input)
    return res


def part2(data: str):
    input = parse(data)
    res = 0
    inner_res = 0
    count = 0

    while True:
        for y in range(138):
            for x in range(138):
                print(input[complex(x, y)], end="")
            print()
        print(count)
        inner_res, input = remove_paper_rolls(input)
        count += 1
        res += inner_res

        if inner_res == 0:
            break
    
    return res
