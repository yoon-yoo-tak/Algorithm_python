import sys

input = sys.stdin.readline

class Agent:
    def __init__(self, code_name = "", score = 0):
        self.code_name = code_name
        self.score = score

spys = []
for i in range(5):
    c_name, s_score = input().split()
    spys.append(Agent(c_name, int(s_score)))

min_idx = 0
for i in range(1, 5):
    if spys[min_idx].score > spys[i].score:
        min_idx = i
print(spys[min_idx].code_name, spys[min_idx].score)