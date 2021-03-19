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
            timestamp = int(f.readline().strip())
            values = f.readline().strip().split(",")
            bus_ids = [{"value": int(values[i]), "index": i} 
                for i in range(len(values))
                if values[i] != "x"]

        min = timestamp
        min_id = None
        for bus in bus_ids:
            waiting_time = bus["value"] - (timestamp % bus["value"])
            if waiting_time < min:
                min = waiting_time
                min_id = bus["value"]
        return min * min_id

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            timestamp = int(f.readline().strip())
            values = f.readline().strip().split(",")
            bus_ids = [{"value": int(values[i]), "index": i} 
                for i in range(len(values))
                if values[i] != "x"]

        time, step = 1, 1
        for bus in bus_ids:
            while (time + bus["index"]) % bus["value"] != 0:
                time += step
            step *= bus["value"]
        return time

