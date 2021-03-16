import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "0xVector"
        self.REPO_URL = "https://github.com/0xVector/AdventOfCode2020"
        self.FILENAME = "solutions/solution_2.py"
        #global vars for solutions:
        self.part2 = 0

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip().replace(".", "") for line in file]

        part1 = 0
        containing_gold = set()

        def check(bag_color):
            for inner_bag in bags[bag_color]:
                if inner_bag[0] in containing_gold or inner_bag[0] == "shiny gold":
                    containing_gold.add(bag_color)
                    return True
                if check(inner_bag[0]):
                    return True


        def dig(bag_name, stack, count_):
            stack.append(count_)
            prod = 1
            for i in stack:  # TODO REDUCE
                prod *= i

            if len(bags[bag_name]) == 0:
                return

            for bag_ in bags[bag_name]:
                dig(bag_[0], stack[:], bag_[1])


        #  Parse data into a dict
        bags = {}
        for line in data:
            line = line.replace(".", "").replace("bags", "").replace("bag", "").strip()
            line = line.split("contain")
            outer__color = line[0].strip()
            inner_colors = line[1].strip()

            bags[outer__color] = []

            for color_entry in inner_colors.split(","):
                if color_entry == "no other":
                    continue
                count = int(color_entry.strip()[0])
                color = color_entry.strip()[2:]
                bags[outer__color].append((color, count))

        for bag in bags:
            if check(bag):
                part1 += 1
        return part1



    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as file:
            data = [line.strip().replace(".", "") for line in file]

        containing_gold = set()

        def check(bag_color):
            for inner_bag in bags[bag_color]:
                if inner_bag[0] in containing_gold or inner_bag[0] == "shiny gold":
                    containing_gold.add(bag_color)
                    return True
                if check(inner_bag[0]):
                    return True

        def dig(bag_name, stack, count_):
            stack.append(count_)
            prod = 1
            for i in stack:  # TODO REDUCE
                prod *= i
            self.part2 += prod

            if len(bags[bag_name]) == 0:
                return

            for bag_ in bags[bag_name]:
                dig(bag_[0], stack[:], bag_[1])

        #  Parse data into a dict
        bags = {}
        for line in data:
            line = line.replace(".", "").replace("bags", "").replace("bag", "").strip()
            line = line.split("contain")
            outer__color = line[0].strip()
            inner_colors = line[1].strip()

            bags[outer__color] = []

            for color_entry in inner_colors.split(","):
                if color_entry == "no other":
                    continue
                count = int(color_entry.strip()[0])
                color = color_entry.strip()[2:]
                bags[outer__color].append((color, count))

        self.part2 = 0
        dig("shiny gold", [], 1)
        self.part2 -= 1  
        return self.part2
  