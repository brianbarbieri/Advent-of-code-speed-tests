import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import re
import operator
from functools import reduce
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
            rules, rest = data[:data.index("")], data[data.index("")+1:]
            nearby_tickets = [[int(n) for n in elem.split(",")]  for elem in rest[rest.index("")+2:]]
            nearby_tickets = reduce(operator.concat, nearby_tickets)

        re_string = "\d+"
        ranges = set()
        for rule in rules:
            nums = list(map(int,re.findall(re_string, rule)))
            ranges.update(set(range(nums[0], nums[1])))
            ranges.update(set(range(nums[2], nums[3])))
        not_found = set(nearby_tickets) - ranges
        summation = 0
        for nf in not_found:
            summation+= nf * nearby_tickets.count(nf)
        return summation

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            rules, rest = data[:data.index("")], data[data.index("")+1:]
            my_ticket = [int(n) for n in rest[:rest.index("")][-1].split(",")]
            nearby_tickets = [[int(n) for n in elem.split(",")]  for elem in rest[rest.index("")+2:]] 

        re_string = "\d+"
        ranges = set()
        for rule in rules:
            nums = list(map(int,re.findall(re_string, rule)))
            ranges.update(set(range(nums[0], nums[1])))
            ranges.update(set(range(nums[2], nums[3])))

        valid_nearby_tickets = []
        for nt in nearby_tickets:
            not_found = set(nt) - ranges
            if not not_found:
                valid_nearby_tickets.append(nt)
        valid_nearby_tickets = np.array(valid_nearby_tickets)

        rule_dict = {}
        for rule in rules:
            name = rule.split(":")[0]
            nums = list(map(int,re.findall(re_string, rule)))
            ranges = [*range(nums[0], nums[1]+1)] + [*range(nums[2], nums[3]+1)]
            rule_dict[name] = ranges

        poss = {k : [] for k in rule_dict.keys()}
        for i in range(valid_nearby_tickets.shape[1]):
            for key in rule_dict.keys():
                if not set(valid_nearby_tickets[:,i]) - set(rule_dict[key]):
                    poss[key].append(i) 

        answer_keys = {}
        while poss.keys():
            single_keys = [k for k in poss.keys() if len(poss[k]) == 1]
            for k in single_keys:
                ans = poss[k][0]
                answer_keys[k] = ans
                del poss[k]     
                for key in poss.keys():
                    try:
                        poss[key].remove(ans)
                    except: pass
        mult = 1
        for key in answer_keys.keys():
            if "departure" in key:
                mult *= my_ticket[answer_keys[key]]
        return mult
