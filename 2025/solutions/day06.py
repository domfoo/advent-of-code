# solutions/day06.py

from operator import add, mul
from functools import reduce


def part1(data: str):
    res = 0
    lines = [line.split() for line in data.splitlines()]
    num_lines = lines[:len(lines)-1]
    ops = lines[len(lines)-1]
    
    for i in range(len(ops)):
        acc = []
        for num_line in num_lines:
            acc.append(int(num_line[i]))
        op = add if ops[i] == "+" else mul
        res += reduce(op, acc)
    
    return res


# suboptimal solution but I wanna go to bed
def part2(data: str):
    res = 0
    lines = [list(line) for line in data.splitlines()]
    num_lines = lines[:len(lines)-1]
    ops = [add if op == "+" else mul for op in "".join(lines[len(lines)-1]).split()]
    op_counter = 0
    acc = []

    for i in range(len(num_lines[0])):
        inner_acc = []
        for num_line in num_lines:
            if num_line[i] != " ":
                inner_acc.append(num_line[i])
        if inner_acc:
            acc.append(int("".join(inner_acc)))
        else:
            op = ops[op_counter]
            res += reduce(op, map(int, acc))
            op_counter += 1
            acc = []
            inner_acc = []
    op = ops[op_counter]
    res += reduce(op, map(int, acc))
    
    return res


if __name__ == "__main__":
    test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
"""

    print("Test Part 1:", part1(test_data))
    print("Test Part 2:", part2(test_data))
