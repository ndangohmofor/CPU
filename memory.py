from time import time


# Memory class used to create different types of
# memory within the simulation

class Memory:
    def __init__(self, name="", access_time=0):
        self.name = name
        self.access_time = access_time
        self.exec_time = 0

    # Output read messages and update process execution
    # time
    def read(self, output=True):
        if output:
            print(f" - {self.name} read: ", end="")
        self.exec_time += self.access_time

    # Output write message and update the process execution
    # time
    def write(self, output=True):
        if output:
            print(f" - {self.name} write: ", end="")
        self.exec_time += self.access_time

    # Placeholder method
    def get_exec_time(self):
        return 0


# Memory class used for the main memory data storage
class MainMemory(Memory):
    def __init__(self):
        Memory.__init__(self, name="Main memory", access_time=30)
        self.data = [""] * 16

    # Return data from main memory address
    def read(self, address):
        data = self.data[address]
        super().read()
        return data

    # Write data to main memory address
    def write(self, address, data):
        self.data[address] = data
        super().write()

    # Return the total execution time
    def get_exec_time(self):
        return self.exec_time

