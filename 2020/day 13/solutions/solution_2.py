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
           data = [line.strip() for line in file]

        depart_time = int(data[0])
        buses = [int(number) for number in data[1].split(",") if number != "x"]
        best_time = 0
        for bus in buses:
            time_to_wait = abs(depart_time - ((depart_time // bus + 1) * bus))
            if time_to_wait < best_time or not best_time:
                best_time = time_to_wait
                best_bus = bus
        return best_bus * best_time

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]

        self.increment = 1
        buses = [(int(value), offset) for offset, value in enumerate(data[1].split(",")) if value.isnumeric()]
        part2 = buses[0][0]
        for bus in buses:
            part2 = self.find(part2, bus[0], bus[1])
            self.increment *= bus[0]
        return part2

    def find(self, ans, bus_value, bus_offset):
        while True:
            if (ans + bus_offset) % bus_value == 0:
                return ans
            ans += self.increment