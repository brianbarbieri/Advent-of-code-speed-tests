import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [p.replace("\n", "") for p in r.readlines()]

        rules, passwords = zip(*[dp.split(":")for dp in data])
        counts = 0
        for rule, password in zip([rule.split(" ") for rule in rules], passwords):
            minr, maxr = rule[0].split("-")
            minr, maxr = int(minr), int(maxr)
            counts += int(minr <= password.count(rule[1]) <= maxr)
        return counts

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [p.replace("\n", "") for p in r.readlines()]

        rules, passwords = zip(*[dp.split(":")for dp in data])
        counts = 0
        for rule, password in zip([rule.split(" ") for rule in rules], passwords):
            password = password.strip()
            minr, maxr = rule[0].split("-")
            minr, maxr = int(minr), int(maxr)
            counts += int(password[minr-1] == rule[1]) ^ int(password[maxr-1] == rule[1])
        return counts