# day10.py

def find_trails(grid, xy, trail):
    if grid[xy] == '9':
        return [trail]
    else:
        trails = []
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            n_xy = (xy[0] + d[0], xy[1] + d[1])
            if int(grid.get(n_xy, 0)) - int(grid.get(xy)) == 1:
                trails += find_trails(grid, n_xy, trail + [n_xy])
        return trails


def part1(data: str) -> int:
    grid = { (x, y): c for y, l in enumerate(data.split("\n")) for x, c in enumerate(l.strip()) }
    trailheads = [xy for xy in grid if grid[xy] == '0']

    return sum(len(set(trail[-1] for trail in find_trails(grid, xy, []))) for xy in trailheads)


def part2(data: str) -> int:
    grid = { (x, y): c for y, l in enumerate(data.split("\n")) for x, c in enumerate(l.strip()) }
    trailheads = [xy for xy in grid if grid[xy] == '0']

    return sum(len(find_trails(grid, xy, [])) for xy in trailheads)
