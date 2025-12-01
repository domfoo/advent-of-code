# solutions/day01.py


def parse(data: str) -> [int]:
    return [int(line.replace("R", "").replace("L", "-")) for line in data.splitlines()]

def part1(data: str) -> int:
    result = 0
    dial = 50

    ops = parse(data)

    for num in ops:
        dial = (dial + num) % 100

        if dial == 0:
            result += 1

    return result


def part2(data: str):
    result = 0
    dial = 50

    ops = parse(data)

    for num in ops:
        new = dial + num
        result += abs(new) // 100 
        if (dial and new <= 0):
            result += 1

        dial = new % 100

    return result


if __name__ == "__main__":
    test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))

    easter_egg = "434C49434B"
    print(f"easter egg: {bytes.fromhex(easter_egg).decode("utf-8")}")
