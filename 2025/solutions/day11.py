# solutions/day11.py

import time
from functools import cache


def benchmark(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fn.__name__}: {end - start:.6f}s")
        return result
    return wrapper

def path_exists(graph: dict[str, list[str]], start: str, end: str) -> bool:
    visited = {start}
    todo = [start]

    while todo:
        node = todo.pop()
        if node == end:
            return True
        for child in graph.get(node, []):
            if child not in visited:
                todo.append(child)
                visited.add(child)
    
    return False


def count_paths(graph: dict[str, list[str]], start: str, end: str):
    @cache
    def dfs(node: str) -> int:
        if node == end:
            return 1

        total = 0
        for child in graph.get(node, []):
            total += dfs(child)
        return total

    return dfs(start)


def parse(data: str) -> dict[str, list[str]]:
    res = dict()
    for line in data.splitlines():
        key, value = line.split(": ")
        res[key] = value.split()
    return res


@benchmark
def part1(data: str):
    graph = parse(data)
    return count_paths(graph, "you", "out")


@benchmark
def part2(data: str):
    graph = parse(data)
    a, b, c, d = "svr", "fft", "dac", "out"

    if not path_exists(graph, b, c):
        b, c = c, b

    return count_paths(graph, a, b) * count_paths(graph, b, c) * count_paths(graph, c, d)


if __name__ == "__main__":
    test_data1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

    test_data2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

    print("Test Part 1:", part1(test_data1))
    print("Test Part 2:", part2(test_data2))
