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
            data = [int(num) for num in f.readline().split(",")]
        return self.play(data, 2020)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            data = [int(num) for num in f.readline().split(",")]
        return self.play(data, 30000000)

    def play(self,  input: list, turns: int) -> int:
        mem = {val: idx + 1 for idx, val in enumerate(input)}
        prev = input[-1]
        for turn in range(len(input) + 1, turns + 1):
            next = 0 if prev not in mem else turn - 1 - mem[prev]
            mem[prev] = turn - 1
            prev = next
        return prev