import sys

input = sys.stdin.readline


class Info:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

n = int(input())
ls = [list(map(int, input().split())) + [i + 1] for i in range(n)]
dist = sorted([Info(x, y, num) for x, y, num in ls], key=lambda x:(abs(x.x - 0) + abs(x.y - 0)))

for i in dist:
    print(i.num)

