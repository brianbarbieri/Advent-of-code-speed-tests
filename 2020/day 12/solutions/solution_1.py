import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:


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

        direction = {
            0 : "N",
            90 : "W",
            180 : "S",
            270 : "E"
        }
        x_s, y_s, a = 0, 0, 270
        for ins in instructions:
            x, d = ins

            if x in ["L",  "R"]:
                if x == "L":
                    a += d
                else:
                    a -= d
                a %= 360
            elif x == "F":
                x = direction[a]

            if x == "N":
                y_s += d
            elif x == "W":
                x_s += d
            elif x == "S":
                y_s -= d
            elif x == "E":
                x_s -= d

        return abs(x_s) + abs(y_s)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            instructions = [(d[0], int(d[1:])) for d in data]

        x_w, y_w, x_s, y_s = 10, 1, 0, 0
        for i, (ins) in enumerate(instructions):
            x, d = ins
            if x == "L":
                if d == 90:
                    x_w, y_w = -y_w, x_w
                elif d == 180:
                    x_w, y_w = -x_w, -y_w
                elif d == 270:
                    x_w, y_w = y_w, -x_w
            elif x == "R":
                if d == 90:
                    x_w, y_w = y_w, -x_w
                elif d == 180:
                    x_w, y_w = -x_w, -y_w
                elif d == 270:
                    x_w, y_w = -y_w, x_w
            elif x == "F":
                x_s += x_w * d
                y_s += y_w * d
            elif x == "N":
                y_w += d
            elif x == "W":
                x_w -= d
            elif x == "S":
                y_w -= d
            elif x == "E":
                x_w += d

        return abs(x_s) + abs(y_s)
