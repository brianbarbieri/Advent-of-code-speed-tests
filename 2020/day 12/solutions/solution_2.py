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
        #global vars for solutions:

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
           data = [line.strip() for line in file]
           instructions = [(line[0], int(line[1:])) for line in data]

        direction = 90  # east
        x, y = 0, 0
        for instruction in instructions:
            letter = instruction[0]
            value = instruction[1]
            if letter == "N":
                y += value
            elif letter == "S":
                y -= value
            elif letter == "E":
                x += value
            elif letter == "W":
                x -= value
            elif letter == "R":
                direction += value
            elif letter == "L":
                direction -= value
            elif letter == "F":
                if direction == 0:  # north
                    y += value
                elif direction == 90:  # east
                    x += value
                elif direction == 180:  # south
                    y -= value
                elif direction == 270:  # west
                    x -= value
            direction %= 360
        return abs(x) + abs(y)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]
            instructions = [(line[0], int(line[1:])) for line in data]

        x, y = 0, 0
        waypoint_x, waypoint_y = 10, 1
        for instruction in instructions:
            letter = instruction[0]
            value = instruction[1]
            if letter == "N":
                waypoint_y += value
            elif letter == "S":
                waypoint_y -= value
            elif letter == "E":
                waypoint_x += value
            elif letter == "W":
                waypoint_x -= value
            elif letter == "R":
                for i in range(int(value / 90)):  # switch for each 90° turn
                    waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            elif letter == "L":
                for i in range(int(value / 90)):  # switch for each 90° turn
                    waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            elif letter == "F":
                x += waypoint_x * value
                y += waypoint_y * value
        return abs(x) + abs(y)

