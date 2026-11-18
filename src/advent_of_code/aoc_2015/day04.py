# day04.py

from hashlib import md5


def search(s: str, secret: str) -> int:
    i = 1
    while True:
        candidate = secret + str(i)
        if md5(candidate.encode()).hexdigest().startswith(s):
            break
        i += 1

    return i


def part1(data: str) -> int:
    return search("00000", data)

def part2(data: str) -> int:
    return search("000000", data)
