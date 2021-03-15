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
            seat_ids = [int(line[:-1].replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in f.readlines()]
        return max(seat_ids)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            seat_ids = [int(line[:-1].replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in f.readlines()]
        for i in range(min(seat_ids), max(seat_ids)):
            if i not in seat_ids and (i - 1) in seat_ids and (i + 1) in seat_ids:
                return i