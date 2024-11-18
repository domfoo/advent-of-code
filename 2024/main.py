# main.py

import sys
import importlib


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
        print(f"Error: Input file for day {day} not found")
        return

    if hasattr(module, "part1"):
        print(f"Day {day}, Part 1: {module.part1(data)}")
    
    if hasattr(module, "part2"):
        print(f"Day {day}, Part 2: {module.part2(data)}")


def main():
    if len(sys.argv) != 2:
        print("Please provide the day number as a command-line argument (e.g., 'python main.py 1').")
        return
        
    day = int(sys.argv[1])
    if day in range(1, 26):
        run(day)
    else:
        print("Advent season runs from December 1 to December 25")


if __name__ == "__main__":
    main()
