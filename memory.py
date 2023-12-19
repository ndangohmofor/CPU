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
