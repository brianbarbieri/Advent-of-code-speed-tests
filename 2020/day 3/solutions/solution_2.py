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
            grid = [line[0:-1] for line in file]

        width = len(grid[0])
        def check(right, bottom):
            x, y = 0, 0
            count = 0
            while not y >= len(grid) - 1:
                x += right
                y += bottom
                if x >= width:
                    x -= width
                if grid[y][x] == "#":
                    count += 1
            return count
        return check(3, 1)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            grid = [line[0:-1] for line in file]

        width = len(grid[0])
        def check(right, bottom):
            x, y = 0, 0
            count = 0
            while not y >= len(grid) - 1:
                x += right
                y += bottom
                if x >= width:
                    x -= width
                if grid[y][x] == "#":
                    count += 1
            return count
        return check(1, 1) * check(3, 1) * check(5, 1) * check(7, 1) * check(1, 2)