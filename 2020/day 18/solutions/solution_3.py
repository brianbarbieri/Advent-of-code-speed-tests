import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
from itertools import product


class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "Akumatic"
        self.REPO_URL = "https://github.com/Akumatic/Advent-of-Code"
        self.FILENAME = "solutions/solution_3.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            inp = [line.strip() for line in f.readlines()]
        return sum([self.parse(line) for line in inp])

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            inp = [line.strip() for line in f.readlines()]
        return sum([self.parse(line, precedence=True) for line in inp])

    def evaluate(self, values: list, operators: list, precedence: bool) -> int:
        if not precedence: # "+" and "*" have same precedence levels
            result = int(values[0])
            for i in range(len(operators)):
                if operators[i] == "+":
                    result += int(values[i+1])
                else: # operators[i] == "*"
                    result *= int(values[i+1])

        else: # "+" and "*" have different precedence levels; "+" evaluated before "*"
            while True:
                try:
                    idx = operators.index("+")
                    values = values[:idx] + [values[idx] + values[idx+1]] + values[idx+2:]
                    operators = operators[:idx] + operators[idx+1:]
                except ValueError:
                    break

            result = 1
            for factor in values:
                result *= factor

        return result

    def parse(self, expression: str, precedence: bool = False) -> int:
        expression = expression.replace(" ", "")
        values = list()
        operators = list()
        i = 0
        while i < len(expression):
            if expression[i] == "+":
                operators.append("+")
                i += 1
            elif expression[i] == "*":
                operators.append("*")
                i += 1
            elif expression[i] == "(":
                # find correct closing bracket
                layer = 1
                j = i + 1
                while j < len(expression):
                    if expression[j] == "(":
                        layer += 1
                    elif expression[j] == ")":
                        if layer == 1:
                            break
                        layer -= 1
                    j += 1
                # evaluate expression between brackets
                values.append(self.parse(expression[i+1:j], precedence))
                i += j - i + 1
            else: # numbers
                j = i
                value =  0
                while j < len(expression) and expression[j].isnumeric():
                    value = value * 10 + int(expression[j])
                    j += 1
                values.append(value)
                i += j - i
        
        return self.evaluate(values, operators, precedence)

