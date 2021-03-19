import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
import numpy as np 
from functools import reduce

class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "brianbarbieri"
        self.REPO_URL = "https://github.com/brianbarbieri/adventofcode2020"
        self.FILENAME = "solutions/solution_1.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            data = [l.replace("\n", "") for l in r.readlines()]
            earliest_time = int(data[0])
            busses = np.array([int(x) for x in data[1].replace("x,", "").split(",")])

        till_arrival =  busses - (earliest_time % busses)
        bus_to_take, to_wait = busses[till_arrival.argmin()], till_arrival.min()
        return bus_to_take * to_wait
            

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as r:
            lines = list(map(lambda line: line.rstrip(), r.readlines()))

        inds_and_nums = [(ind, int(elem)) for ind, elem in enumerate(lines[1].split(',')) if elem != 'x']

        rests, divisors = [], []
        for (ind, num) in inds_and_nums:
            rests.append((-ind) % num)
            divisors.append(num)

        return self.chinese_remainder(rests, divisors)

    def chinese_remainder(self, remainders, divisors):
        M = self.prod(divisors)
        as_ = list(map(lambda d: int(M / d), divisors))
        eea_results = map(lambda tup: self.extended_gcd(*tup), zip(as_, divisors))
        is_ = [result[0] % div for result, div in zip(eea_results, divisors)]
        Z = sum(map(self.prod, zip(is_, remainders, as_)))
        x = Z % M
        return x

    def prod(self, nums):
        return reduce(lambda a, b: a * b, nums, 1)

    def extended_gcd(self, a, b):
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1

        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return old_s, old_t, old_r # return Bezout coefficient 1, 2, and the gcd