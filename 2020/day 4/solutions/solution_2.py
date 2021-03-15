import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]

        data.append("")  # we need empty line after last, and it gets .stripped()

        REQUIRED_ENTRIES = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

        # Parse data into dicts
        passports, passport = [], {}

        for line in data:
            if line == "":
                passports.append(passport)
                passport = {}

            else:
                fields = line.split()

                for field in fields:
                    field = field.split(":")
                    passport[field[0]] = field[1]


        # Part 1
        part1 = 0
        for passport in passports:
            if all(val in passport for val in REQUIRED_ENTRIES):
                part1 += 1
        return part1


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip() for line in file]

        data.append("")  # we need empty line after last, and it gets .stripped()

        REQUIRED_ENTRIES = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

        # Parse data into dicts
        passports, passport = [], {}

        for line in data:
            if line == "":
                passports.append(passport)
                passport = {}

            else:
                fields = line.split()

                for field in fields:
                    field = field.split(":")
                    passport[field[0]] = field[1]

        part2 = 0
        for passport in passports:

            try:
                byr = 2002 >= int(passport["byr"]) >= 1920
                iyr = 2020 >= int(passport["iyr"]) >= 2010
                eyr = 2030 >= int(passport["eyr"]) >= 2020
                hcl = passport["hcl"].startswith("#") and len(passport["hcl"]) == 7
                ecl = passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
                pid = len(passport["pid"]) == 9 and passport["pid"].isnumeric()

                # Throw ValueError if not in correct format
                int(passport["hcl"][1:], 16)  # Convert to int from hex

                # hgt checks
                height = int(passport["hgt"][:-2])
                if passport["hgt"].endswith("cm"):
                    hgt = 193 >= height >= 150

                elif passport["hgt"].endswith("in"):
                    hgt = 76 >= height >= 59

                else:  # Doesn't end with unit
                    hgt = False

                if all((byr, iyr, eyr, hgt, hcl, ecl, pid)):
                    part2 += 1

            except (KeyError, ValueError):  # Something isn't there
                pass
        return part2