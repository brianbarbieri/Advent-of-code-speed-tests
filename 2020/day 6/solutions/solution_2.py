import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"
        self.FILENAME = "solutions/solution_2.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]

        data.append("")
        # Parse the data into list of groups
        groups, group = [], []
        for line in data:
            if line == "":
                groups.append(group)
                group = []
            else:
                group.append(line)
        return sum(len(set.union(*map(set, group))) for group in groups)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]
                
        data.append("")
        # Parse the data into list of groups
        groups, group = [], []
        for line in data:
            if line == "":
                groups.append(group)
                group = []
            else:
                group.append(line)
        return sum(len(set.intersection(*map(set, group))) for group in groups)

