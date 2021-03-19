import sys, os
sys.path.append(os.path.abspath('../day 12'))
from baseclass import Solution

# imports required for solution:
from solutions.solution_1_cython import part_1, part_2

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            instructions = [(d[0], int(d[1:])) for d in data]
        return part_1(instructions)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            instructions = [(d[0], int(d[1:])) for d in data]
            return part_2(instructions)