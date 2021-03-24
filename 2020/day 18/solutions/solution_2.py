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
            data = [line.strip().replace(" ", "") for line in file]

        part1 = 0
        for line in data:
            stack = [0]
            operation_stack = []
            operation = "+"

            for char in line:
                if char.isnumeric():
                    if operation == "+":
                        stack[-1] += int(char)

                    elif operation == "*":
                        stack[-1] *= int(char)

                elif char in {"+", "*"}:
                    operation = char

                elif char == "(":
                    operation_stack.append(operation)
                    stack.append(0)
                    operation = "+"

                elif char == ")":
                    answer = stack.pop()
                    operation = operation_stack.pop()
                    if operation == "+":
                        stack[-1] += answer
                    elif operation == "*":
                        stack[-1] *= answer

            part1 += stack[0]
        return part1



    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip().replace(" ", "") for line in file]

        part2 = 0

        for line in data:

            stack = [0]
            operation_stack = [None]
            operation = "+"

            for char in line:

                if char.isnumeric():
                    if operation == "+":
                        stack[-1] += int(char)

                elif char == "*":
                    if operation_stack[-1] == "*":  # End * group
                        operation_stack.pop()
                        answer = stack.pop()
                        stack[-1] *= answer

                    operation_stack.append("*")  # Start new * group
                    operation = "+"
                    stack.append(0)

                elif char == "+":
                    operation = "+"

                elif char == "(":
                    operation_stack.append(operation)
                    operation = "+"
                    stack.append(0)

                elif char == ")":
                    answer = stack.pop()
                    operation = operation_stack.pop()

                    if operation == "+":
                        stack[-1] += answer
                    elif operation == "*":
                        stack[-1] *= answer

                        # Do it again if we have multiplication ending just before a closing parenthesis
                        answer = stack.pop()
                        operation = operation_stack.pop()

                        if operation == "+":
                            stack[-1] += answer
                        elif operation == "*":
                            stack[-1] *= answer

            if len(stack) > 1:  # Finish everything up if some numbers left in the stack
                for i in stack:
                    answer = stack.pop()
                    operation = operation_stack.pop()

                    if operation == "+":
                        stack[-1] += answer

                    elif operation == "*":
                        stack[-1] *= answer

            part2 += stack[0]
        return part2