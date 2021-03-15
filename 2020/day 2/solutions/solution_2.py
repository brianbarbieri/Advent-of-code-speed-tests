import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line for line in file]

        # Part 1 ===
        part1 = 0
        for entry in data:

            entry = entry.split()
            numbers = entry[0].split(sep="-")

            minimum = int(numbers[0])
            maximum = int(numbers[1])

            letter = entry[1][0]
            password = entry[2]

            if minimum <= password.count(letter) <= maximum:
                part1 += 1
        return part1


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line for line in file]

        part2 = 0
        for entry in data:

            entry = entry.split()
            numbers = entry[0].split(sep="-")

            pos1 = int(numbers[0])-1
            pos2 = int(numbers[1])-1

            letter = entry[1][0]
            password = entry[2]

            first = password[pos1] == letter
            second = password[pos2] == letter

            # XOR
            if first ^ second:
                part2 += 1
        return part2