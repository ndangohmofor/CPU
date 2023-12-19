from memory import Memory
from time import time


class Register(Memory):
    def __init__(self):
        Memory.__init__(self, name="Register", access_time=0.1)
        self.data = {"r0": None, "r1": None}

    def read(self, address):
        super().read(output=False)
        return self.data[address]

    def write(self, address, data):
        super().write(output=False)
        self.data[address] = data

    def get_exec_time(self):
        return self.exec_time
