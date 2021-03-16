import os
import json
from sklearn.preprocessing import minmax_scale
import numpy as np

days = [name for name in os.listdir(os.path.dirname(__file__)) if os.path.isdir(os.path.join(os.path.dirname(__file__), name)) and name.startswith("day")]
scores = []
for day in days:
    with open(os.path.join(os.path.dirname(__file__), day, "scores.json")) as f:
        scores.append(json.load(f))        

table_data = {}
repos = list(scores[0].keys())
for score in scores:
    part_1_score = np.array([score[key]["time_part_1"] for key in repos]).reshape(1, -1)
    part_1_score = 1 - minmax_scale(part_1_score, axis=1).flatten()
    part_2_score = np.array([score[key]["time_part_2"] for key in repos]).reshape(1, -1)
    part_2_score = 1 - minmax_scale(part_2_score, axis=1).flatten()
    for i in range(len(repos)):
        table_data[repos[i]] = part_1_score[i] + part_2_score[i] + table_data.get(repos[i], 0)

readmd = f'## Performance scoring of the advent of code 2020\n| Github repo | Score |\n| ------------- | ------------- |\n'
for repo in sorted(table_data.items(), key=lambda item: item[1], reverse=True):
    readmd += f"| [{repo[0]}]({scores[0][repo[0]]['url']}) | {round(repo[1], 2)} / {len(scores)*2} |\n"

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'w') as writer:
    writer.write(readmd)
print("Saved highscore to README.md")