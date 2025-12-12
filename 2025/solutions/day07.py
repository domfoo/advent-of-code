# solutions/day07.py

from pprint import pprint
import time


def benchmark(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fn.__name__}: {end - start:.6f}s")
        return result
    return wrapper


@benchmark
def part1(data: str):
    lines = [list(line) for line in data.splitlines()[0::2]]
    # pprint(["".join(line) for line in lines])
    beams = [0] * len(lines[0])
    beams[lines[0].index("S")] = 1
    split_counter = 0

    for line in lines[1:]:
        for i, c in enumerate(line):
            if beams[i]:
                if c == "^":
                    split_counter += 1
                    beams[i] = 0
                    if not beams[i+1]:
                        beams[i+1] = 1
                        # line[i+1] = "|"
                    if not beams[i-1]:
                        beams[i-1] = 1
                        # line[i-1] = "|"
                # if c == ".":
                #     line[i] = "|"
    
    # pprint(["".join(line) for line in lines])
    return split_counter


@benchmark
def part2(data: str):
    lines = [list(line) for line in data.splitlines()[0::2]]
    beams = [0] * len(lines[0])
    beams[lines[0].index("S")] = 1

    for line in lines[1:]:
        for i, c in enumerate(line):
            if beams[i]:
                if c == "^":
                    beams[i+1] += beams[i]
                    # line[i+1] = "|"
                    beams[i-1] += beams[i]
                    # line[i-1] = "|"
                    beams[i] = 0
                # if c == ".":
                #     line[i] = "|"

    return sum(beams)


if __name__ == "__main__":
    test_data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
