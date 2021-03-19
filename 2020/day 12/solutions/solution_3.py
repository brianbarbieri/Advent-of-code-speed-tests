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
            data = [line.strip() for line in f.readlines()]

        x, y = 0, 0
        dirs = ((1,0), (0, 1), (-1, 0), (0, -1))
        idx = 0
        for instruction in data:
            action = instruction[0]
            value = int(instruction[1:])
            if action == "N":
                y += value
            elif action == "S":
                y -= value
            elif action == "E":
                x += value
            elif action == "W":
                x -= value
            elif action == "F":
                x += dirs[idx][0] * value
                y += dirs[idx][1] * value
            else: # action in ("R", "L")
                sig = 1 if action == "L" else -1
                idx = (idx + sig * value // 90) % 4
        return abs(x) + abs(y)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            data = [line.strip() for line in f.readlines()]

        x, y, wx, wy = 0, 0, 10, 1
        dirs = ((1,1), (-1, 1), (-1, -1), (1, -1))
        idx = 0
        for instruction in data:
            action = instruction[0]
            value = int(instruction[1:])
            if action == "N":
                wy += value
            elif action == "S":
                wy -= value
            elif action == "E":
                wx += value
            elif action == "W":
                wx -= value
            elif action == "F":
                x += wx * value
                y += wy * value
            else: # action in ("R", "L")
                sig = 1 if action == "L" else -1
                for _ in range(value // 90):
                    idx_prev, idx = idx, (idx + sig) % 4
                    tmp_wx = wx
                    wx = wy * dirs[idx_prev][1] * dirs[idx][0]
                    wy = tmp_wx * dirs[idx_prev][0] * dirs[idx][1]
        return abs(x) + abs(y)

