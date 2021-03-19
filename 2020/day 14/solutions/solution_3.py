import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "Akumatic"
        self.REPO_URL = "https://github.com/Akumatic/Advent-of-Code"
        self.FILENAME = "solutions/solution_3.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            data =  [line.strip().split(" = ") for line in f.readlines()]
        return sum(self.run_v1(data).values())

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            data =  [line.strip().split(" = ") for line in f.readlines()]
        return sum(self.run_v2(data).values())

    def recursive_floating_bits(self, value: int, idx: list) -> list:
        if len(idx) == 1:
            return [value | (1 << idx[0]), value & ~(1 << idx[0])]
        return self.recursive_floating_bits(value | (1 << idx[0]), idx[1:]) + \
            self.recursive_floating_bits(value & ~(1 << idx[0]), idx[1:])

    def mask_index(self, value: int, mask: str) -> list:
        # if bitmask bit is 1, memory address bit is overwritten with 1
        value |= int(mask.replace("X", "0"), 2)
        # take care of all floating bits
        positions = [35 - i for i, char in enumerate(mask) if char == "X"]
        return self.recursive_floating_bits(value, positions)

    def run_v2(self, input: list) -> dict: 
        memory = dict()
        mask = None
        for instruction in input:
            if instruction[0] == "mask":
                mask = instruction[1]
            else: # instruction[0][:3] == "mem"
                value = int(instruction[1])
                indices = self.mask_index(int(instruction[0][4:-1]), mask)
                for idx in indices:
                    memory[idx] = value
        return memory

    def run_v1(self, input: list) -> dict:
        mask_and, mask_or = None, None
        memory = dict()
        for instruction in input:
            if instruction[0] == "mask":
                mask_and = int(instruction[1].replace("X", "1"), 2)
                mask_or = int(instruction[1].replace("X", "0"), 2)
            else: # instruction[0][:3] == "mem"
                idx = int(instruction[0][4:-1])
                value = (int(instruction[1]) & mask_and) | mask_or
                memory[idx] = value
        return memory
    