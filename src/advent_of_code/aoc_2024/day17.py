# day17.py

from itertools import count


class Machine():
    def __init__(self, data: str):
        self.data = data
        self.reset()


    def reset(self):
        self.pc = 0
        self.out = []

        lines = self.data.splitlines()
        self.regA = int(lines.pop(0).split(": ")[-1])
        self.regB = int(lines.pop(0).split(": ")[-1])
        self.regC = int(lines.pop(0).split(": ")[-1])
        lines.pop(0)
        self.program = [int(x) for x in lines.pop(0).split(": ")[-1].split(",")]


    def execute(self) -> str:
        while self.pc < len(self.program) - 1:
            opcode = self.program[self.pc]
            operand = self.program[self.pc + 1]

            match opcode:
                case 0:
                    operand = self.to_combo_operand(operand)
                    self.regA = self.regA // 2**operand
                    self.pc += 2
                case 1:
                    self.regB = self.regB ^ operand
                    self.pc += 2
                case 2:
                    operand = self.to_combo_operand(operand)
                    self.regB = operand % 8
                    self.pc += 2
                case 3:
                    if self.regA:
                        self.pc = operand
                    else:
                        self.pc += 2
                case 4:
                    self.regB = self.regB ^ self.regC
                    self.pc += 2
                case 5:
                    operand = self.to_combo_operand(operand)
                    self.out.append(operand % 8)
                    self.pc += 2
                case 6:
                    operand = self.to_combo_operand(operand)
                    self.regB = self.regA // 2**operand
                    self.pc += 2
                case 7:
                    operand = self.to_combo_operand(operand)
                    self.regC = self.regA // 2**operand
                    self.pc += 2
                case _:
                    print("Illegal opcode")
                    self.pc += 2
        return self.out


    def find_regA(self) -> int:
        # terrible brute force, please don't judge
        for c in count():
            self.regA = c
            if self.program == self.execute():
                return c
            self.reset()

    
    def to_combo_operand(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.regA
            case 5:
                return self.regB
            case 6:
                return self.regC
            case _:
                print("Illegal combo operand")
                return operand


    def __str__(self) -> str:
        return f"regA: {self.regA}\nregB: {self.regB}\nregC: {self.regC}\n\nProgram: {self.program}"


def part1(data: str) -> str:
    machine = Machine(data)
    print(machine)
    return ",".join(map(str, machine.execute()))


def part2(data: str) -> str:
    machine = Machine(data)
    print(machine)
    return machine.find_regA()


if __name__ == "__main__":
    test_data = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

    test_data = """Register A: 66
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

#     test_data = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

    print("Test Part 1:", part1(test_data))
    # print("Test Part 2:", part2(test_data))
