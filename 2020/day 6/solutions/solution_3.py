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
            groups = [line.split() for line in f.read().strip().split("\n\n")]

        def count(groups: list, everyone: bool) -> int:
            result = 0
            for group in groups:
                answers = {chr(c):0 for c in range(97, 123)}

                for answer in group:
                    for letter in answer:
                        answers[letter] += 1

                if everyone:
                    result += sum([1 for letter in answers if answers[letter] == len(group)])
                else:
                    result += sum([1 for letter in answers if answers[letter]])

            return result

        return count(groups, False)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            groups = [line.split() for line in f.read().strip().split("\n\n")]

        def count(groups: list, everyone: bool) -> int:
            result = 0
            for group in groups:
                answers = {chr(c):0 for c in range(97, 123)}

                for answer in group:
                    for letter in answer:
                        answers[letter] += 1

                if everyone:
                    result += sum([1 for letter in answers if answers[letter] == len(group)])
                else:
                    result += sum([1 for letter in answers if answers[letter]])

            return result

        return count(groups, True)