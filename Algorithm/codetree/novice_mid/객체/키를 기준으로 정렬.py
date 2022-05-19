import sys

input = sys.stdin.readline


class Info:
    def __init__(self, name = "", height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())
ls = [list(input().split()) for _ in range(n)]
student = sorted([Info(name, height, weight) for name, height, weight in ls], key=lambda x: x.height)

for i in student:
    print(i.name, i.height, i.weight)
