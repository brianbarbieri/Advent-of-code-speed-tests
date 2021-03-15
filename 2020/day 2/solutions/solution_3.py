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
            vals = list()
            for line in f.readlines():
                txt = line.split()
                nums = txt[0].split("-")
                vals.append((int(nums[0]), int(nums[1]), txt[1][:1], txt[2]))

        cnt = 0
        for val in vals:
            min, max, char, text = val # for better readability
            char_cnt = text.count(char)
            if char_cnt >= min and char_cnt <= max:
                cnt += 1
        return cnt


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            vals = list()
            for line in f.readlines():
                txt = line.split()
                nums = txt[0].split("-")
                vals.append((int(nums[0]), int(nums[1]), txt[1][:1], txt[2]))

        cnt = 0
        for val in vals:
            pos_a, pos_b, char, text = val # for better readability
            if (char == text[pos_a - 1]) ^ (char == text[pos_b - 1]):
                cnt += 1
        return cnt
