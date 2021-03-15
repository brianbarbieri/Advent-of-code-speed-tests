import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

class Solution_Repo(Solution):


    def __init__(self):
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = sorted([int(p.replace("\n", "")) for p in r.readlines()])

        mini = 0
        maxi = -1
        while mini != len(data):
            if data[mini] + data[maxi] == 2020:
                return data[mini] * data[maxi]
            elif data[mini] + data[maxi] > 2020:
                maxi -= 1
            else:
                mini += 1

    def part_2(self):
        import numpy as np

        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = np.array(sorted([int(p.replace("\n", "")) for p in r.readlines()]))

        i = 0
        data = data[i+1:][data[i+1:] + data[i] < 2020]
        j, k = np.where(np.add.outer(data,data) + data[i] == 2020)[0]
        return data[i] * data[j] * data[k]
