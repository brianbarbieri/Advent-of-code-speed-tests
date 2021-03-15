import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import numpy as np 

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [[c for c in p.replace("\n", "")] for p in r.readlines()]
            max_x, max_y = len(data), len(data[0])
            data = [p*max_x for p in data]

        def traverse(x,y):
            return x+1, y+3

        pos = (0,0)
        trees = 0
        while pos[0] < max_x-1:
            pos = traverse(*pos)
            trees += int(data[pos[0]][pos[1]] == "#")
        return trees

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [[c for c in p.replace("\n", "")] for p in r.readlines()]
            max_x, max_y = len(data), len(data[0])
            data = [p*max_x for p in data]

        def traverse(x,y, add_x, add_y):
            return x+add_x, y+add_y

        trees = []
        combis = [[1,1],[1,3],[1,5],[1,7],[2,1]]
        for add_x, add_y in combis:
            pos = (0,0)
            tres = 0
            while pos[0] < max_x-1:
                pos = traverse(pos[0], pos[1], add_x, add_y)
                tres += int(data[pos[0]][pos[1]] == "#")
            trees.append(tres)
                
        return np.prod(trees)
