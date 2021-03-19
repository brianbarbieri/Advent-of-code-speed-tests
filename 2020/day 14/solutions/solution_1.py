import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import numpy as np 
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

        regex = "\[(\d+)\] = (\d+)"
        memory = {}
        mask = None
        for com in data:
            if "mask" in com:
                mask = com.split(" = ")[-1]      
                bin_mask = np.array([True if p != "X" else False for p in mask])
                mask = np.array([-1 if p == "X" else int(p)for p in mask])
            else:
                mem_loc, value = map(int, re.search(regex, com).groups())
                bin_val = np.array([int(s) for s in '{0:036b}'.format(value)])
                bin_val[bin_mask] = mask[bin_mask]
                dec_val = int("".join(bin_val.astype(str)), 2)
                memory[mem_loc] =  dec_val
        return sum(memory.values())
            

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()] 

        regex = "\[(\d+)\] = (\d+)"
        memory = {}
        mask = None
        for com in data:
            if "mask" in com:
                mask = com.split(" = ")[-1]      
                mask = [p for p in mask]
            else:
                mem_loc, value = map(int, re.search(regex, com).groups())
                bin_loc = np.array([int(s) for s in '{0:036b}'.format(mem_loc)])
                masked_loc = []
                for loc, ma in zip(bin_loc, mask):
                    if (ma == "X") or (ma == "1"):
                        masked_loc.append(ma)
                    else:
                        masked_loc.append(str(loc))
                addresses = self.unfloat("".join(masked_loc))
                for ad in addresses:
                    memory[int(ad, 2)] =  value
        return sum(memory.values())
            

    def unfloat(self, string):
        combs = [string]
        while "X" in "".join(combs):
            addrs = combs.pop(0)
            idx = addrs.find("X")
            for c in ["0", "1"]:
                addrs_l = [c for c in addrs]
                addrs_l[addrs.find("X")] = c
                combs.append("".join(addrs_l))
        return combs 