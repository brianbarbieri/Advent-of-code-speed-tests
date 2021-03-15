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

        seats = []
        for passport in data:
            lower = 0  # F
            upper = 127  # B
            # Row
            for i in range(7):
                mid = (lower + upper) / 2
                if passport[i] == "F":
                    upper = int(mid)
                elif passport[i] == "B":
                    if not mid.is_integer():  # Dividing odd numbers produces float, add 1 to truncate correctly
                        mid += 1
                    lower = int(mid)
            row = lower
            # Col
            lower = 0  # L
            upper = 7  # R
            for i in range(7, 10):
                mid = (lower + upper) / 2
                if passport[i] == "L":
                    upper = int(mid)
                elif passport[i] == "R":
                    if not mid.is_integer():
                        mid += 1
                    lower = int(mid)
            col = lower
            seat_id = row * 8 + col
            seats.append(seat_id)
        return max(seats)


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]
        
        seats = []
        for passport in data:
            lower = 0  # F
            upper = 127  # B
            # Row
            for i in range(7):
                mid = (lower + upper) / 2
                if passport[i] == "F":
                    upper = int(mid)
                elif passport[i] == "B":
                    if not mid.is_integer():  # Dividing odd numbers produces float, add 1 to truncate correctly
                        mid += 1
                    lower = int(mid)
            row = lower
            # Col
            lower = 0  # L
            upper = 7  # R
            for i in range(7, 10):
                mid = (lower + upper) / 2
                if passport[i] == "L":
                    upper = int(mid)
                elif passport[i] == "R":
                    if not mid.is_integer():
                        mid += 1
                    lower = int(mid)
            col = lower
            seat_id = row * 8 + col
            seats.append(seat_id)
        seats.sort()

        count = seats[0]
        for i in range(len(seats)):
            if count != seats[i]:
                break
            count += 1
        return count
