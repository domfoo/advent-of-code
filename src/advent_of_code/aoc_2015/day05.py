# day05.py

from itertools import pairwise


def check2b(s: str) -> bool:
    arr = map("".join, zip(iter(s), iter(s[1:]), iter(s[2:])))
    return any(a == c for a, _, c in arr)


def check2a(s: str) -> bool:
    arr = map("".join, pairwise(s))
    return any(s.count(pair) >= 2 for pair in arr)


def check1c(s: str) -> bool:
    return all(sub not in s for sub in ["ab", "cd", "pq", "xy"])


def check1b(s: str) -> bool:
    arr = list(s)
    for i, c in enumerate(arr[:len(arr)-1]):
        if c == arr[i + 1]:
            return True
    return False


def check1a(s: str) -> bool:
    return sum(s.count(vowel) for vowel in list("aeiou")) >= 3


def part1(data: str) -> int:
    return sum(check1a(line) and check1b(line) and check1c(line) for line in data.splitlines())


def part2(data: str) -> int:
    return sum(check2a(line) and check2b(line) for line in data.splitlines())
