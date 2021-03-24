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
            data = [l.replace("\n", "") for l in r.readlines()]

        summation = 0
        for formula in data:
            summation += self.calculate(formula, self.left_to_right_solvep1)
        return summation

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]

        summation = 0
        for formula in data:
            summation += self.calculate(formula, self.left_to_right_solve_p2)
        return summation

    def left_to_right_solvep1(self, formula):
        reg_digit = "(\d+)"
        reg_operator = "([+*])"
        digits = re.findall(reg_digit, formula)
        operators = re.findall(reg_operator, formula)
        result = int(digits[0])
        for i in range(1,len(operators)+1):
            if operators[i-1] == "+":
                result += int(digits[i])
            else:
                result *= int(digits[i])
        return str(result)

    
    def left_to_right_solve_p2(self, formula):
        reg_plus = "(\d+ \+ \d+)"
        while "+" in formula:
            plus = [(m.start(0), m.end(0)) for m in re.finditer(reg_plus, formula)][0]
            s, e = plus
            formula = formula[:s]+ self.left_to_right_solvep1(formula[s:e]) + formula[e:]
        return self.left_to_right_solvep1(formula)

    def calculate(self, s, calc_method):
        inner_most_bracket_regex = "\([^()]+\)"
        while "(" in s:
            found_brackets = re.findall(inner_most_bracket_regex, s)
            for bracket in found_brackets:
                s =s[:s.find(bracket)] + calc_method(bracket[1:-1]) + s[s.find(bracket)+len(bracket):]
        return int(calc_method(s))
