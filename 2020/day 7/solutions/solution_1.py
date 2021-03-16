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
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "").replace("bags", "bag").replace("bag", "bags") for l in r.readlines()]

        # first split input up in dict with bagcol(key) in bagcols(list of values)
        # start with splitting up on contain:
        data_c = [line.split(" contain ") for line in data]
        bag_regex = r"[0-9]+ ([a-z ]+)"
        bag_dict = {}
        for bag in data_c:
            
            bags = re.findall(bag_regex, bag[-1])
            
            for bg in bags:
                if bg not in bag_dict:
                    bag_dict[bg] = set()
                bag_dict[bg].add(bag[0])

        # now start with the "shiny gold bags" and iterate to see which bags to add
        found_bags = set()
        to_add = ["shiny gold bags"]
        while len(to_add) > 0:
            current_bag = to_add.pop()
            new_bags = bag_dict.get(current_bag)
            if new_bags is not None:
                for bag in new_bags:
                    found_bags.add(bag)
                to_add += new_bags
        return len(found_bags)
            

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "").replace("bags", "bag").replace("bag", "bags") for l in r.readlines()]   

        class Bag:
            def __init__(self, colour, value, multifactor, childeren):
                self.colour = colour
                self.value = value
                self.multifactor = multifactor
                self.childeren = childeren

            def __repr__(self):
                return str([self.colour, self.value, self.multifactor, self.childeren])

            def calculate_value(self):
                return self.value*self.multifactor

        data_c = [line.split(" contain ") for line in data]
        bag_regex = r"([0-9]+) ([a-z ]+)"

        bag_dict = {}
        for bag in data_c:
            bags = re.findall(bag_regex, bag[-1])
            bag_dict[bag[0]] = bags
            
        score = -1
        bag_collection = [Bag("shiny gold bags", 1, 1, bag_dict["shiny gold bags"])]
        while len(bag_collection) > 0:
            current_bag = bag_collection.pop()
            score += current_bag.multifactor
            for child in current_bag.childeren:
                bag_collection.append(
                    Bag(child[-1], int(child[0]), current_bag.multifactor*int(child[0]), bag_dict[child[-1]])
                )
        return score