import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import re

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "Akumatic"
        self.REPO_URL = "https://github.com/Akumatic/Advent-of-Code"
        self.FILENAME = "solutions/solution_3.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            vals = list()
            for data in f.read()[:-1].split("\n\n"):
                vals.append(dict(d.split(":") for d in data.replace("\n", " ").split()))

        def assert_fields(data: dict) -> bool:
            return all((k in data for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")))

        valid_passes = [val for val in vals if assert_fields(val)]
        return len(valid_passes)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            vals = list()
            for data in f.read()[:-1].split("\n\n"):
                vals.append(dict(d.split(":") for d in data.replace("\n", " ").split()))

        def assert_fields(data: dict) -> bool:
            return all((k in data for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")))

        valid_passes = [val for val in vals if assert_fields(val)]
        patterns = {
            "byr": "19[2-9][0-9]|200[0-2]",
            "iyr": "20(1[0-9]|20)",
            "eyr": "20(2[0-9]|30)",
            "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
            "hcl": "#[0-9a-f]{6}",
            "ecl": "amb|blu|brn|gry|grn|hzl|oth",
            "pid": "[0-9]{9}",
            "cid": ".*"
        }
        return sum((all((re.fullmatch(patterns[v], val[v]) for v in val)) for val in valid_passes))+1
