import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
from itertools import product

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"
        self.FILENAME = "solutions/solution_2.py"
        #global vars for solutions:


    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
           data = [line.strip().replace("[", " ").replace("]", " ").replace("=", " ") for line in file]
           commands = [line.split() for line in data]

        part1 = 0
        memory = {}
        for command in commands:
            if command[0] == "mask":
                mask = command[1][::-1]
            else:
                address = int(command[1])
                value = command[2]
                new_value = list('0'*36 + str(bin(int(value)))[2:])[::-1]
                for i, vals in enumerate(zip(mask, new_value)):
                    mask_char = vals[0]
                    if mask_char != "X":
                        new_value[i] = mask_char
                new_value = "".join(new_value)[::-1]
                memory[address] = new_value
        for entry in memory.values():
            part1 += int(entry, 2)
        return part1

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip().replace("[", " ").replace("]", " ").replace("=", " ") for line in file]
            commands = [line.split() for line in data]

        memory = {}
        for command in commands:
            if command[0] == "mask":
                mask = command[1][::-1]
            else:
                address = command[1]
                value = int(command[2])
                new_address = list('0'*36 + str(bin(int(address)))[2:])[::-1]
                for i, vals in enumerate(zip(mask, new_address)):
                    mask_char, address_char = vals
                    if mask_char != "0":
                        new_address[i] = mask_char
                adress_combination = new_address[:]
                for comb in product((1, 0,), repeat=mask.count("X")):
                    adress_combination = new_address[:]
                    count = 0
                    for i, char in enumerate(new_address):
                        if char == "X":
                            adress_combination[i] = str(comb[count])
                            count += 1
                    adress_combination = int("".join(adress_combination)[::-1], 2)
                    memory[adress_combination] = value
                    count = 0
        return sum(memory.values())
