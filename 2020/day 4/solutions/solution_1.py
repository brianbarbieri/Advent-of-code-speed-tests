import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import re

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = r.readlines()
            passports = "".join(data).split("\n\n")
            passports = [dict([attr.split(":") for attr in re.split(' |\n', passport)]) for passport in passports]

        required_attr = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        valid_passports = 0
        for passport in passports:
            valid_passports += int(set(required_attr) <= passport.keys())
        return valid_passports


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = r.readlines()
            passports = "".join(data).split("\n\n")
            passports = [dict([attr.split(":") for attr in re.split(' |\n', passport)]) for passport in passports]

        required_attr = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        valid_passports = 0
        for passport in passports:
            if set(required_attr) <= passport.keys():
                bv = (1920 <= int(passport.get("byr")) <= 2002)
                iv = (2010 <= int(passport.get("iyr")) <= 2020)
                iv2 = (2020 <= int(passport.get("eyr")) <= 2030)
                
                height_re = r"([0-9]+)(in)|([0-9]+)(cm)"
                mtch = re.match(height_re, passport.get("hgt"))
                if mtch is None:
                    hv = False
                else:
                    if mtch.groups()[0]:
                        hv = 59 <= int(mtch.groups()[0]) <= 76
                    elif mtch.groups()[2]:
                        hv = 150 <= int(mtch.groups()[2]) <= 193
                    else:
                        hv = False
                colour_re= r"#[0-9a-f]{0,6}"
                mtch = re.search(colour_re, passport.get("hcl"))
                cv = mtch is not None and len(passport.get("hcl")) == 7

                ev =  passport.get("ecl") in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
                
                pass_re =  r"[0-9]{9}"
                mtch = re.search(pass_re, passport.get("pid"))
                pv = mtch is not None and len(passport.get("pid")) == 9

                valid_passports += int(bv and iv and iv2 and hv and cv and ev and pv)
        return valid_passports