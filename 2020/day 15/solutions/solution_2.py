import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
from collections import deque

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"
        self.FILENAME = "solutions/solution_2.py"
        #global vars for solutions:
        self.part2 = 0

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]

        numbers = list(map(int, data[0].split(",")))
        number_indices = {number: deque([i], maxlen=2) for i, number in enumerate(numbers)}
        starting_number_count = len(number_indices)
        return self.play(2020, numbers, number_indices, starting_number_count)


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]

        numbers = list(map(int, data[0].split(",")))
        number_indices = {number: deque([i], maxlen=2) for i, number in enumerate(numbers)}
        starting_number_count = len(number_indices)
        return self.play(30000000, numbers, number_indices, starting_number_count)

    def play(self, n, numbers, number_indices, starting_number_count):
        for i in range(starting_number_count, n):

            last = numbers[-1]

            if len(number_indices[last]) >= 2:
                last_spoken = number_indices[last][1]
                last_last_spoken = number_indices[last][0]
                new = last_spoken - last_last_spoken
            else:
                new = 0
            numbers.append(new)

            if new not in number_indices:
                number_indices[new] = deque(maxlen=2)

            number_indices[new].append(i)

        return new
