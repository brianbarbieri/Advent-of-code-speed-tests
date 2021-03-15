import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
from itertools import combinations

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"
        self.FILENAME = "solutions/solution_2.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [int(line) for line in file]

        for combo in combinations(data, 2):
            if combo[0] + combo[1] == 2020:
                return combo[0] * combo[1]

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [int(line) for line in file]

        for combo in combinations(data, 3):
            if combo[0] + combo[1] + combo[2] == 2020:
                return combo[0] * combo[1] * combo[2]