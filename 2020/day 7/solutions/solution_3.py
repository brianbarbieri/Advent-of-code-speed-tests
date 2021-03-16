import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "Akumatic"
        self.REPO_URL = "https://github.com/Akumatic/Advent-of-Code"
        self.FILENAME = "solutions/solution_3.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            inp = [line.strip() for line in f.read().strip().split("\n")]

        def parseRules(input) -> dict:
            rules = {}
            amount = {}
            for line in input:
                rule = line.strip(".").split(" contain ")
                bag = rule[0][:-(4 if rule[0][-1]=="g" else 5)]
                if rule[1] == "no other bags":
                    rules[bag] = []
                    amount[bag] = []
                else:
                    contents = [r.split() for r in rule[1].split(", ")]
                    rules[bag] = [" ".join(c[1:3]) for c in contents]
                    amount[bag] = [int(c[0]) for c in contents]
            return rules, amount

        def can_contain(rules: dict, rule, bag, cache):
            if rule in cache:
                return cache[rule]
            if bag in rules[rule]:
                cache[rule] = True
            else:
                cache[rule] = any(can_contain(rules, b, bag, cache) for b in rules[rule])
            return cache[rule]

        def count_bags(rules: dict, amount: dict, bag, cache):
            if bag in cache:
                return cache[bag]

            if len(rules[bag]) == 0:
                cache[bag] = 0
                return 0
            else:
                sum = 0
                for i in range(len(rules[bag])):
                    sum += amount[bag][i] * (count_bags(rules, amount, rules[bag][i], cache) + 1)
                cache[bag] = sum
                return cache[bag]

        cache = {}
        rules, amount = parseRules(inp)
        return sum([can_contain(rules, rule, "shiny gold", cache) for rule in rules])


    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            inp = [line.strip() for line in f.read().strip().split("\n")]

        def parseRules(input) -> dict:
            rules = {}
            amount = {}
            for line in input:
                rule = line.strip(".").split(" contain ")
                bag = rule[0][:-(4 if rule[0][-1]=="g" else 5)]
                if rule[1] == "no other bags":
                    rules[bag] = []
                    amount[bag] = []
                else:
                    contents = [r.split() for r in rule[1].split(", ")]
                    rules[bag] = [" ".join(c[1:3]) for c in contents]
                    amount[bag] = [int(c[0]) for c in contents]
            return rules, amount

        def can_contain(rules: dict, rule, bag, cache):
            if rule in cache:
                return cache[rule]
            if bag in rules[rule]:
                cache[rule] = True
            else:
                cache[rule] = any(can_contain(rules, b, bag, cache) for b in rules[rule])
            return cache[rule]

        def count_bags(rules: dict, amount: dict, bag, cache):
            if bag in cache:
                return cache[bag]

            if len(rules[bag]) == 0:
                cache[bag] = 0
                return 0
            else:
                sum = 0
                for i in range(len(rules[bag])):
                    sum += amount[bag][i] * (count_bags(rules, amount, rules[bag][i], cache) + 1)
                cache[bag] = sum
                return cache[bag]

        rules, amount = parseRules(inp)
        cache = {}
        return count_bags(rules, amount, "shiny gold", cache)


