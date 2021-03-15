import timeit
import json
import os

class Solution:

    def __init__(self):
        self.REPO_OWNER = ""
        self.REPO_URL = ""
        self.DAY = 1
        self.YEAR = 2020

    def part_1(self):
        pass

    def part_2(self):
        pass

    def assert_solution(self):

        with open(os.path.dirname(__file__) + '/solution.txt', "r") as r:
            solution_1, solution_2 = r.readline().split(",")
            print(f"Running the solutions of {self.REPO_OWNER}({self.REPO_URL})")

            assert solution_1 == str(self.part_1()), f"Answer incorrect: answer is {solution_1}, your answer is {str(self.part_1())}"
            assert solution_2 == str(self.part_2()), f"Answer incorrect: answer is {solution_2}, your answer is {str(self.part_2())}"
            print("Solutions to both parts of the problem are correct")

            time_part1 = timeit.timeit(self.part_1, number=1000) / 1000
            print(f"Finished timing part 1: {time_part1}")
            time_part2 = timeit.timeit(self.part_2, number=1000) / 1000
            print(f"Finished timing part 2: {time_part2}")
            self.save_times(time_part1, time_part2)
            
    def format_run_time(self, s):
        if s <= 1:
            return str(round(s *1000, 4)) + " (ms)"
        elif s <= 0.001:
            return str(round(s *1000000, 4)) + " (μs)"
        elif s <= 0.000001:
            return str(round(s *1000000000, 4)) + " (ns)"
        else:
            return  str(round(s, 4)) + "(s)"


    def save_times(self, time_part1, time_part2):

        with open(os.path.dirname(__file__) + '/scores.json', 'r') as r:
            scores = json.load(r)

        repo_times = {
            "time_part_1" : time_part1,
            "time_part_2" : time_part2,
            "time_mean" : (time_part1 + time_part2) / 2,
            "url" : self.REPO_URL
        }

        scores[self.REPO_OWNER] = repo_times
        with open(os.path.dirname(__file__) + '/scores.json', 'w') as f:
            json.dump(scores, f)
        
        readmd = f'## Scoring for day {self.DAY} of the advent of code {self.YEAR}\n| Github repo | Score part 1 | Score part 2 |\n| ------------- | ------------- | ------------- |\n'

        for w in sorted(scores, key=lambda x: scores[x]['time_mean']):
            sp1 = self.format_run_time(scores[w]['time_part_1'])
            sp2 = self.format_run_time(scores[w]['time_part_2'])
            readmd += f"| [{w}]({scores[w]['url']}) | {sp1} | {sp2} |\n"

        with open('README.md', 'w') as writer:
            writer.write(readmd)
        print("Saved run to README.md")
