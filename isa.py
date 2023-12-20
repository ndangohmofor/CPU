from time import time

from register import Register


class ISA:
    def __init__(self):
        self.memory = None
        self.registers = Register()
        self.instructions = {
            "lb": self.load_b,
            "sb": self.store,
            "li": self.load_i,
            "j": self.jump
        }
        self.output = ""

    def get_exec_time(self):
        exec_time = self.registers.get_exec_time()

        if self.memory is not None:
            exec_time += self.memory.get_exec_time()

        return exec_time

    def set_memory(self, memory):
        self.memory = memory

    def read_instructions(self, file):
        if self.memory is not None:
            print(f"ISA memory: {self.memory.name}")
            start = time()
            with open(file) as code_file:
                code = code_file.readline()
                lines = [line.strip() for line in code if line.strip() != '']
                for line in lines:
                    self.parse_line(line)
            return time() - start
        else:
            print("Architecture has found no memory")
            return None

    def parse_line(self, line):
        tokens = line.split(" ")
        inst = tokens[0]
        if inst == "lb" or inst == "sb":
            print(f"{line}", end="")
        arg1 = tokens[1]
        if len(tokens) == 2 and inst == "li":
            arg2 = " "
            self.instructions[inst](arg1, arg2)
        elif len(tokens) > 2:
            arg2 = tokens[2]
            self.instructions[inst](arg1, arg2)
        else:
            self.instructions[inst](arg1)

    def load_b(self, arg1, arg2):
        address = int(self.registers.read(arg2))
        data = self.memory.read(address)
        self.registers.write(arg1, data)
        if data is not None:
            print(data)

    def store(self, arg1, arg2):
        data = self.registers.read(arg1)
        address = int(self.registers.read(arg2))
        self.memory.write(address, data)
        if data is not None:
            print(f" {data}")

    def load_i(self, arg1, arg2):
        self.registers.write(arg1, arg2)

    def jump(self, arg1):
        if arg1 == "100":
            data = self.registers.read('r0')
            if data is not None:
                self.output += data
            else:
                print("- NO DATA")
        else:
            print("Jump address is not recognized.")
