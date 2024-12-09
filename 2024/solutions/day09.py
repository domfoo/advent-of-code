# day09.py
import numpy


def part1(data: str) -> str:
    data = [int(i) for i in data]

    blocks = numpy.zeros(sum(data), dtype=numpy.uint64)
    spare = []
    add = 0
    for ix, size in enumerate(data):
        if ix % 2:
            if size:
                spare.extend(range(add, add+size))
        else:
            file_id = ix // 2
            blocks[add:add+size] = file_id
        add += size

    rd_ptr = len(blocks) - 1
    wr_ptr = spare.pop(0)
    while rd_ptr > wr_ptr:
        blocks[wr_ptr] = blocks[rd_ptr]
        blocks[rd_ptr] = 0
        
        wr_ptr = spare.pop(0)
        rd_ptr -= 1
        while (rd_ptr > wr_ptr) and (blocks[rd_ptr] == 0):
            rd_ptr -= 1

    return sum(ix * val for ix, val in enumerate(blocks))


def part2(data: str) -> str:
    data = [int(i) for i in data]
    blocks = numpy.zeros(sum(data), dtype=numpy.uint64)
    files = []
    spare = []
    add = 0
    for ix, size in enumerate(data):
        if ix % 2:
            if size:
                spare.append((add, size))
        else:
            file_id = ix // 2
            files.append((file_id, add, size))
        add += size
    
    file_ptr = len(files) - 1
    while file_ptr > 0:
        file_id, add, size = files[file_ptr]
        if add < spare[0][0]:   # No more space available
            break
        
        relocate = False
        for ix, (start, length) in enumerate(spare):
            if (length >= size) and (start < add):
                relocate = True
                break
        if relocate:
            files[file_ptr] = (file_id, start, size)
            if size == length:
                spare.pop(ix)
            else:
                spare[ix] = (start + size, length - size)
        file_ptr -= 1
    
    for file_id, add, size in files:
        blocks[add:add+size] = file_id

    return sum(ix * val for ix, val in enumerate(blocks))
