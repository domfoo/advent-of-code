from pathlib import Path
import importlib
from argparse import ArgumentParser, ArgumentTypeError


def load_input(year: int, day: int) -> str:
    with open(f"input/{year}/{day:02}.txt") as f:
        return f.read().strip()


def run(year: int, day: int):
    try:
        module = importlib.import_module(f"advent_of_code.aoc_{year}.day{day:02}")
    except ModuleNotFoundError:
        print(f"Error: Solution for {day:02}.12.{year} not found")
        return

    try:
        data = load_input(year, day)
    except FileNotFoundError:
        print(f"Input file for {day:02}.12.{year} not found")
        return

    if hasattr(module, "part1"):
        print(f"{day:02}.12.{year}, Part 1: {module.part1(data)}")
    
    if hasattr(module, "part2"):
        print(f"{day:02}.12.{year}, Part 2: {module.part2(data)}")


def parse_args() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("year", type=int, choices=range(2015, 2026+1), help="Provide the year (e.g., 'uv run 2015 1').")
    parser.add_argument("day", type=int, help="Provide the day (e.g., 'uv run 2015 1').")
    args = parser.parse_args()

    max_day = 25 if args.year <= 2024 else 12

    if not 1 <= args.day <= max_day:
        parser.error(f"--day must be between 1 and {max_day} for year {args.year}")
    return args



def main() -> None:
    args = parse_args()
    run(args.year, args.day)
