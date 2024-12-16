# day16.py

from pprint import pprint
from collections import deque
import heapq


type Graph = dict[complex: list[complex]]


def bfs(graph: Graph, start: complex, end: complex):
    marked = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return marked
        # yield node
        marked.add(node)
        queue.extend(n for n in graph[node] if n not in marked)


def dijkstra(graph: Graph, start: complex, end: complex):
    # Distanz-Map: speichert die kürzesten Distanzen zu jedem Knoten
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Queue für die Breitensuche (enthält aktuelle Knoten)
    queue = deque([start])

    # Vorgänger-Map: zum Nachverfolgen des Pfades
    predecessors = {node: None for node in graph}

    while queue:
        current = queue.popleft()

        # Gehe alle Nachbarn des aktuellen Knotens durch
        for neighbor, direction in graph[current]:
            weight = 1 if direction.imag != 0 else 1000
            # weight = current - previous
            # Wenn ein kürzerer Pfad gefunden wird
            if distances[neighbor] > distances[current] + weight:
                distances[neighbor] = distances[current] + weight
                predecessors[neighbor] = current
                queue.append(neighbor)

    # Pfad zurückverfolgen, falls ein Ziel gefunden wurde
    path = []
    if distances[end] != float('inf'):
        while end is not None:
            path.append(end)
            end = predecessors[end]
        path.reverse()

    return path, distances


def parse(data: str) -> tuple[Graph, complex, complex]:
    grid = {x + y * 1j: val for y, line in enumerate(data.split('\n')) for x, val in enumerate(line) if val != "#"}
    graph = {pos: [] for pos, x in grid.items()}
    for p in graph:
        for next_dir in [1, -1, 1j, -1j]:
            if grid.get(p + next_dir) in [".", "S", "E"]:
                graph[p].append((p + next_dir, next_dir))

    start = min(k for k, v in grid.items() if v == "S")
    end = min(k for k, v in grid.items() if v == "E")
    return grid, graph, start, end


def part1(data: str) -> int:
    grid, graph, start, end = parse(data)
    # pprint(graph)
    # print(start, end)

    #######
    # for node, neighbors in graph.items():
    #     lines = data.split()
    #     lines[int(node.imag)] = lines[int(node.imag)][:int(node.real)] + "A" + lines[int(node.imag)][int(node.real+1):]
    #     for n in neighbors:
    #         lines[int(n.imag)] = lines[int(n.imag)][:int(n.real)] + "B" + lines[int(n.imag)][int(n.real+1):]

    #     print(*lines, sep="\n", end="\n\n")

    lines = data.split()

    path, distances = dijkstra(graph, start, end)

    for node in path:
        lines[int(node.imag)] = lines[int(node.imag)][:int(node.real)] + "P" + lines[int(node.imag)][int(node.real+1):]
        print(*lines, sep="\n", end="\n\n")

    print(distances[end], len(path))

    ########
    # for node in bfs(graph, start, end):
    #     lines[int(node.imag)] = lines[int(node.imag)][:int(node.real)] + "P" + lines[int(node.imag)][int(node.real+1):]
    #     print(*lines, sep="\n", end="\n\n")

    return


def part2(data: str) -> int:
    pass


if __name__ == "__main__":
    test_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
