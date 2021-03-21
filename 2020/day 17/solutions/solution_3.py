import sys, os
sys.path.append(os.path.abspath('../day 1'))
from baseclass import Solution

# imports required for solution:
from itertools import product


class Solution_Repo(Solution):

    def __init__(self):
        Solution.__init__(self)
        self.REPO_OWNER = "Akumatic"
        self.REPO_URL = "https://github.com/Akumatic/Advent-of-Code"
        self.FILENAME = "solutions/solution_3.py"

    def part_1(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            inp = [list(line.strip()) for line in f.readlines()]
            active_cubes = set()
            for y in range(len(inp)):
                for x in range(len(inp[0])):
                    if inp[y][x] == "#":
                        active_cubes.add((x, y, 0, 0))
        return self.simulate(active_cubes, 3)

    def part_2(self):
        with open(os.path.dirname(__file__) + "/../input.txt", "r") as f:
            inp = [list(line.strip()) for line in f.readlines()]
            active_cubes = set()
            for y in range(len(inp)):
                for x in range(len(inp[0])):
                    if inp[y][x] == "#":
                        active_cubes.add((x, y, 0, 0))
        return self.simulate(active_cubes, 4)


    def simulate(self, active_cubes: set, size: int = 3, iterations: int = 6) -> int:
        assert 3 <= size <= 4
        # neighbor positions
        positions = product(range(-1, 2), repeat=size)
        if size == 4:
            npos = tuple(pos for pos in positions if pos != (0, 0, 0, 0))
        else: # size == 4
            npos = tuple((pos[0], pos[1], pos[2], 0) for pos in positions if pos != (0, 0, 0))

        # iterations
        for _ in range(iterations):
            next_active = set()
            neighbors = set()
            # check if active cubes stay active
            for cube in active_cubes:
                count = 0
                for n in npos:
                    pos = tuple(cube[i] + n[i] for i in range(4))
                    if pos in active_cubes:
                        count += 1
                    else:
                        neighbors.add(pos)
                if 2 <= count <= 3:
                    next_active.add(cube)
            # check neighbors of active cubes if they become active
            for cube in neighbors:
                count = 0
                for n in npos:
                    pos = tuple(cube[i] + n[i] for i in range(4))
                    if pos in active_cubes:
                        count += 1
                if count == 3:
                    next_active.add(cube)

            active_cubes = next_active

        return len(active_cubes)