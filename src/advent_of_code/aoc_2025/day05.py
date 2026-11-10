# day05.py

def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x.start)
    merged = [intervals[0]]

    for i, curr in enumerate(intervals[1:]):
        last = merged[-1]
        if curr.start <= last.stop:
            merged[-1] = range(last.start, min(last.stop, curr.stop))
        else:
            merged.append(curr)
    return merged


def parse(data: str):
    parts = data.split("\n\n")

    intervals_lines = parts[0].splitlines()
    intervals = []
    for s in intervals_lines:
        tmp = s.split("-")
        a = int(tmp[0])
        b = int(tmp[1])
        intervals.append(range(a, b))

    ids_lines = parts[1].splitlines()
    ids = [int(s) for s in ids_lines]

    return intervals, ids



def part1(data: str) -> int:
    result = 0
    intervals, ids = parse(data)
    
    for id in ids:
        for interval in intervals:
            if id in interval:
                result += 1
                break

    return result


def part2(data: str):
    result = 0
    intervals, _ = parse(data)
    
    for interval in merge_intervals(intervals):
        result += len(interval)

    return result
