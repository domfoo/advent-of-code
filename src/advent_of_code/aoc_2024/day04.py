# day04.py

def diagonals(l):
    L = l[:]
    return_list = [[] for i in range(len(L))]

    for line in range(len(L)):
        L[line] = L[line][::-1]
        i = line

        for elem in L[line]:
            if i >= len(return_list):
                return_list.append([])

            return_list[i].append(elem)
            i += 1

    return ["".join(line) for line in return_list[::-1]]


def count_string_in_lines(s: str, lines: list[str]):
    return sum(line.count(s) for line in lines)


def part1(data: str) -> int:
    # data = """MMMSXXMASM\
    #           MSAMXMSMSA\
    #           AMXSXMAAMM\
    #           MSAMASMSMX\
    #           XMASAMXAMM\
    #           XXAMMXXAMA\
    #           SMSMSASXSS\
    #           SAXAMASAAA\
    #           MAMMMXMMMM\
    #           MXMXAXMASX"""

    lines_horizontal_forwards = data.split()
    lines_horizontal_backwards = [line[::-1] for line in lines_horizontal_forwards]
    lines_vertical_forwards = ["".join(line) for line in zip(*lines_horizontal_forwards)]
    lines_vertical_backwards = [line[::-1] for line in lines_vertical_forwards]

    all_possible_lines = [
        lines_horizontal_forwards,
        lines_horizontal_backwards,
        lines_vertical_forwards,
        lines_vertical_backwards,
        diagonals(lines_horizontal_forwards),
        diagonals(lines_horizontal_backwards),
        diagonals(lines_horizontal_forwards[::-1]),
        diagonals(lines_horizontal_backwards[::-1])
    ]

    return sum(count_string_in_lines("XMAS", lines) for lines in all_possible_lines)

def part2(data: str) -> int:
    # data = """.M.S......\
    #           ..A..MSMS.\
    #           .M.S.MAA..\
    #           ..A.ASMSM.\
    #           .M.S.M....\
    #           ..........\
    #           S.S.S.S.S.\
    #           .A.A.A.A..\
    #           M.M.M.M.M.\
    #           .........."""

    cnt = 0
    grid = [list(line) for line in data.split()]

    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if value == "A":
                try:
                    tl = grid[row+1][col-1]
                    tr = grid[row+1][col+1]
                    bl = grid[row-1][col-1]
                    br = grid[row-1][col+1]
                except IndexError:
                    continue

                if not all(c in ["M", "S"] for c in [tl, tr, bl, br]):
                    continue

                if tl == br or bl == tr:
                    continue

                print(f"{tr} {tl}\n {value} \n{bl} {br}")
                print()
                cnt+=1

    return cnt