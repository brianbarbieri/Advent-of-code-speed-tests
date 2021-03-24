import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import numpy as np
from solutions.solution_1_cython import change_states_p1, change_states_p2

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            source = np.array([[[int(elem) for elem in l.replace(".", "0").replace("#", "1")] for l in data]])

        for c in range(6):
            next_cycle = np.zeros((source.shape[0]+2, source.shape[1]+2, source.shape[2]+2))
            next_cycle[1:-1,1:-1,1:-1] = source
            source = change_states_p1(next_cycle)
        return int(source.sum())

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            source = np.array([[[[int(elem) for elem in l.replace(".", "0").replace("#", "1")] for l in data]]])

        for c in range(6):
            next_cycle = np.zeros((source.shape[0]+2, source.shape[1]+2, source.shape[2]+2, source.shape[3]+2))
            next_cycle[1:-1,1:-1,1:-1,1:-1] = source
            source = change_states_p2(next_cycle)
        return int(source.sum())