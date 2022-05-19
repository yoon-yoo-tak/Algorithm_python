import sys

input = sys.stdin.readline

class Info:
    def __init__(self, name = "", h = 0, w = 0):
        self.name = name
        self.h = h
        self.w = w

n = int(input())
ls = [list(input().split()) for _ in range(n)]
student = sorted([Info(name, int(h), int(w)) for name, h, w in ls], key=lambda x:(x.h, -x.w))

for i in student:
    print(i.name, i.h, i.w)
