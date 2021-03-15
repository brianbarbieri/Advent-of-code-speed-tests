import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import re

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [p.replace("\n", "") for p in r.readlines()]
            data = [(p[:7], p[7:]) for p in data]

        def partition_string(string, higher_val="B"):
            if higher_val == "B":
                seats = list(range(127+1))
            else:
                seats = list(range(8+1))

            for part in string:
                if part == higher_val:
                    seats = seats[int(len(seats)/2):]
                else:
                    seats = seats[:int(len(seats)/2)]
            return seats[0]

        ids = []
        for seat in data:
            ids.append(partition_string(seat[0]) * 8 + partition_string(seat[1], "R"))
        return max(ids)


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [p.replace("\n", "") for p in r.readlines()]
            data = [(p[:7], p[7:]) for p in data]

        def partition_string(string, higher_val="B"):
            if higher_val == "B":
                seats = list(range(127+1))
            else:
                seats = list(range(8+1))

            for part in string:
                if part == higher_val:
                    seats = seats[int(len(seats)/2):]
                else:
                    seats = seats[:int(len(seats)/2)]
            return seats[0]

        ids = []
        for seat in data:
            ids.append(partition_string(seat[0]) * 8 + partition_string(seat[1], "R"))

        sorted_ids = sorted(ids)
        for i in range(min(sorted_ids), max(sorted_ids)):
            if i not in sorted_ids:
                return i