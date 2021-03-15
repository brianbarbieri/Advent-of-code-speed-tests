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
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = r.read().replace(" ", "\n\n")
            groups = data.split("\n\n")
            groups = [group.split("\n") for group in groups]

        total_score = 0
        for group in groups:
            score = 0
            # char_list = [char for char in "abcdefghijklmnopqrstuvwxyz"]
            found_char_list = []
            for person in group:
                for answer in person:
                    if answer not in found_char_list:
                        score += 1
                        found_char_list.append(answer)
            total_score += score
        return total_score

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = r.read().replace(" ", "\n\n")
            groups = data.split("\n\n")
            groups = [group.split("\n") for group in groups]

        total_score = 0
        for group in groups:
            
            char_dict = {char:0 for char in "abcdefghijklmnopqrstuvwxyz"}
            found_char_list = []
            for person in group:
                for answer in person:
                    char_dict[answer] += 1

            score = 0
            for char in char_dict:
                if char_dict[char] == len(group):
                    score += 1
            total_score += score
        return total_score