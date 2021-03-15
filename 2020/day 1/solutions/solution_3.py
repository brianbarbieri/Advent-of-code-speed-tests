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
            vals =  [int(line[:-1]) for line in f.readlines()]

        for val in vals:
            if (2020 - val) in vals:
                return (2020 - val) * val

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            vals =  [int(line[:-1]) for line in f.readlines()]

        for i in range(len(vals)):
            for j in range(i, len(vals)):
                if (2020 - vals[i] - vals[j]) in vals:
                    return vals[i] * vals[j] *  (2020 - vals[i] - vals[j])