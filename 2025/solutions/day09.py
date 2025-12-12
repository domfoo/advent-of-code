# solutions/day09.py

from itertools import combinations, pairwise
from pprint import pprint


type Point = tuple[int, int]
type Rectangle = tuple[Point, Point]

def my_print(ps: list[Point], cs: list[Point] = None):
    if not cs:
        cs = []
    for i in range(14):
        print(str(i)[-1], end="")
    print()
    for y in range(1,10):
        print(y, end="")
        for x in range(1,14):
            if (x, y) in cs:
                print("@", end="")
            elif (x, y) in ps:
                print("#", end="")
            else:
                print(".", end="")
        print("\n")

def point_in_polygon(point: Point, polygon: list[Point]) -> bool:
    x, y = point
    poly = list(polygon)
    n = len(poly)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i

    return inside

def is_inside(points: set[Point], c: Point) -> bool:
    # print(c)
    # print(c in points)
    # # print(any(p[0] > c[0] and p[1] == c[1] for p in points) and any(p[0] < c[0] and p[1] == c[1] for p in points))
    # print(any(p[0] > c[0] and p[1] == c[1] and any(b[0] == p[0] and b[1] > p[1] for b in points) and any(b[0] == p[0] and b[1] < p[1] for b in points) for p in points) and any(p[0] < c[0] and p[1] == c[1] and any(b[0] == p[0] and b[1] > p[1] for b in points) and any(b[0] == p[0] and b[1] < p[1] for b in points) for p in points))
    # # print(any(p[0] == c[0] and p[1] > c[1] for p in points) and any(p[0] == c[0] and p[1] < c[1] for p in points))
    # print(any(p[0] == c[0] and p[1] > c[1] and any(b[0] > p[0] and b[1] == p[1] for b in points) and any(b[0] < p[0] and b[1] == p[1] for b in points) for p in points) and any(p[0] == c[0] and p[1] < c[1] and any(b[0] > p[0] and b[1] == p[1] for b in points) and any(b[0] < p[0] and b[1] == p[1] for b in points) for p in points))
    # print()

    return (
        c in points or
        any(p[0] > c[0] and p[1] == c[1] and any(b[0] == p[0] and b[1] > p[1] for b in points) and any(b[0] == p[0] and b[1] < p[1] for b in points) for p in points) and any(p[0] < c[0] and p[1] == c[1] and any(b[0] == p[0] and b[1] > p[1] for b in points) and any(b[0] == p[0] and b[1] < p[1] for b in points) for p in points) or 
        any(p[0] == c[0] and p[1] > c[1] and any(b[0] > p[0] and b[1] == p[1] for b in points) and any(b[0] < p[0] and b[1] == p[1] for b in points) for p in points) and any(p[0] == c[0] and p[1] < c[1] and any(b[0] > p[0] and b[1] == p[1] for b in points) and any(b[0] < p[0] and b[1] == p[1] for b in points) for p in points)
    )


def corners(rectangle: Rectangle) -> set[Point]:
    a = rectangle[0]
    b = rectangle[1]
    return {a, b, (a[0], b[1]), (b[0], a[1])}


def area(pair: tuple[Point]) -> int:
    a, b = pair[0], pair[1]
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


def parse(data: str) -> set[Point]:
    return list(tuple(map(int, line.split(","))) for line in data.splitlines())


def part1(data: str):
    points = parse(data)
    rectangles = combinations(points, 2)
    return area(max(rectangles, key=area))


# broke it and I don't know how to fix, got the star anyways
def part2(data: str):
    points = parse(data)
    
    rectangles = list(combinations(points, 2))
    edges = list(pairwise(points + [points[0]]))

    for (x,y), (u,v) in rectangles:
        for (p,q), (r,s) in edges:
            if p>r: p,r = r,p
            if q>s: q,s = s,q

            if p<u and q<v and r>x and s>y:
                return area(((x,y), (u,v)))
    return None
    ###############################
    for rectangle in sorted(rectangles, key=area, reverse=True):
        print(rectangle, area(rectangle))
        my_print(points, rectangle)
        if all(point_in_polygon(c, points) for c in corners(rectangle)):
            return area(rectangle)

    return None

    # valid_rectangles = filter(lambda r: all(is_inside(points, c) for c in corners(r)), rectangles)

    # valid_rectangles = list(valid_rectangles)

    # for r in sorted(valid_rectangles, key=area):
    #     print(r, corners(r), area(r), sep="\n")
    #     my_print(points, r)
    #     print()
    # print([is_inside(points, c) for c in corners(((9,5), (2,3)))])
    # my_print(points, ((9,5), (2,3)))

    # return area(max(valid_rectangles, key=area))


if __name__ == "__main__":
    test_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
