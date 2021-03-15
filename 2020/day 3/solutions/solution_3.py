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
            vals = [line[:-1] for line in f.readlines()]

        def count_trees(vals: list, dx: int, dy: int) -> int:
            x, y, cnt, length, mod = 0, 0, 0, len(vals) - dy, len(vals[0])
            while y < length:
                x = (x + dx) % mod
                y += dy
                if vals[y][x] == "#":
                    cnt += 1
            return cnt

        return count_trees(vals, 3, 1)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            vals = [line[:-1] for line in f.readlines()]

        def count_trees(vals: list, dx: int, dy: int) -> int:
            x, y, cnt, length, mod = 0, 0, 0, len(vals) - dy, len(vals[0])
            while y < length:
                x = (x + dx) % mod
                y += dy
                if vals[y][x] == "#":
                    cnt += 1
            return cnt

        sol_part1 = count_trees(vals, 3, 1)
        deltas = ((1, 1), (5, 1), (7, 1), (1, 2))
        prod = sol_part1
        for delta in deltas:
            prod *= count_trees(vals, delta[0], delta[1])
        return prod