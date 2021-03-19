import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import numpy as np

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [int(l.replace("\n", "")) for l in r.readline().split(",")]

        end_game = 2020
        spoken_numbers = dict(zip(data, range(1, len(data)+1)))

        current_turn = len(data) + 1
        next_number = current_turn - spoken_numbers[data[-1]] - 1

        for i in range(current_turn, end_game+1):
            number_spoken = next_number
            try:
                next_number = i - spoken_numbers[number_spoken]
            except:
                next_number = 0
            spoken_numbers[number_spoken] = i
        return number_spoken

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [int(l.replace("\n", "")) for l in r.readline().split(",")]

        end_game = 30000000
        spoken_numbers = dict(zip(data, range(1, len(data)+1)))

        current_turn = len(data) + 1
        next_number = current_turn - spoken_numbers[data[-1]] - 1

        for i in range(current_turn, end_game+1):
            number_spoken = next_number
            try:
                next_number = i - spoken_numbers[number_spoken]
            except:
                next_number = 0
            spoken_numbers[number_spoken] = i
        return number_spoken