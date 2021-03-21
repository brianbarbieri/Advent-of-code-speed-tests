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
            data = [l.replace("\n", "") for l in r.readlines()]
            source = np.array([[[int(elem) for elem in l.replace(".", "0").replace("#", "1")] for l in data]])

        def change_states(a):
            new_state = np.zeros(a.shape)
            for i in range(a.shape[0]):
                for j in range(a.shape[1]):
                    for k in range(a.shape[2]):
                        kernel_value = a[max(0,i-1):min(a.shape[0], i+2),max(0,j-1):min(a.shape[1], j+2),max(0,k-1):min(a.shape[2], k+2)].sum() - a[i,j,k] 
                        if a[i,j,k] == 1: # if active
                            if kernel_value in [2, 3]:
                                new_state[i,j,k] = 1
                            else:
                                new_state[i,j,k] = 0
                        else: # if not active
                            if kernel_value == 3:
                                new_state[i,j,k] = 1
                            else:
                                new_state[i,j,k] = 0
            return new_state

        for c in range(6):
            next_cycle = np.zeros((source.shape[0]+2, source.shape[1]+2, source.shape[2]+2))
            next_cycle[1:-1,1:-1,1:-1] = source
            source = change_states(next_cycle)
        return int(source.sum())

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            source = np.array([[[[int(elem) for elem in l.replace(".", "0").replace("#", "1")] for l in data]]])

        def change_states(a):
            new_state = np.zeros(a.shape)
            for i in range(a.shape[0]):
                for j in range(a.shape[1]):
                    for k in range(a.shape[2]):
                        for l in range(a.shape[3]):
                            kernel_value = a[max(0,i-1):min(a.shape[0], i+2),max(0,j-1):min(a.shape[1], j+2),max(0,k-1):min(a.shape[2], k+2),max(0,l-1):min(a.shape[3], l+2)].sum() - a[i,j,k,l] 
                            if a[i,j,k,l] == 1: # if active
                                if kernel_value in [2, 3]:
                                    new_state[i,j,k,l] = 1
                                else:
                                    new_state[i,j,k,l] = 0
                            else: # if not active
                                if kernel_value == 3:
                                    new_state[i,j,k,l] = 1
                                else:
                                    new_state[i,j,k,l] = 0
            return new_state

        for c in range(6):
            next_cycle = np.zeros((source.shape[0]+2, source.shape[1]+2, source.shape[2]+2, source.shape[3]+2))
            next_cycle[1:-1,1:-1,1:-1,1:-1] = source
            source = change_states(next_cycle)
        return int(source.sum())