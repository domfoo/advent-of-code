# main.py

import sys
import importlib
import argparse
from pathlib import Path


def create_code_file(code_path):
    code_path.write_text(
        f"# {code_path}\n"
        "\n"
        "\n"
        "def part1(data: str):\n"
        "    pass\n"
        "\n"
        "\n"
        "def part2(data: str):\n"
        "    pass\n"
        "\n"
        "\n"
        "if __name__ == \"__main__\":\n"
        "    test_data = \"\"\"\"\"\"\n"
        "\n"
        "    print(\"Test Part 1:\", part1(test_data))\n"
        "    print(\"Test Part 2:\", part2(test_data))\n"
    )


def load_input(day):
    with open(f"input/day{day:02}.txt") as f:
        return f.read().strip()


def run(day):
    try:
        module = importlib.import_module(f"solutions.day{day:02}")
    except ModuleNotFoundError:
        print(f"Error: Solution for day {day} not found")
        return

    try:
        data = load_input(day)
    except FileNotFoundError:
        print(f"Input file for day {day} not found")
        return

    if hasattr(module, "part1"):
        print(f"Day {day}, Part 1: {module.part1(data)}")
    
    if hasattr(module, "part2"):
        print(f"Day {day}, Part 2: {module.part2(data)}")


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, choices=range(1, 13), help="Provide the day (e.g., 'python main.py 1').")
    parser.add_argument("--new", action="store_true", help="Create a python template for a new day (e.g., 'python main.py 1 --new').")
    return parser.parse_args()
    

def main():
    args = parse_args()

    code_path = Path(f"solutions/day{args.day:02}.py")

    if args.new and not code_path.exists():
        create_code_file(code_path)

    run(args.day)


if __name__ == "__main__":
    main()
