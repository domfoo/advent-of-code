# day02.py

def part1(data: str) -> int:
    result = 0
    dimensions = [tuple(map(int, line.split("x"))) for line in data.splitlines()]
    for l, w, h in dimensions:
        a = l*w
        b = w*h
        c = h*l
        result += 2*a + 2*b + 2*c + min([a, b, c])
    return result

def part2(data: str) -> int:
    result = 0
    dimensions = [tuple(map(int, line.split("x"))) for line in data.splitlines()]
    for l, w, h in dimensions:
        band = sum(sorted((l, w, h))[:2])*2
        ribbon = l * w * h
        result += band + ribbon
    return result
