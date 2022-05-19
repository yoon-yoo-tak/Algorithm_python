import sys

input = sys.stdin.readline

class Info:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

n = int(input())

ls = [list(map(int, input().split())) + [i + 1] for i in range(n)]
student = sorted([Info(h, w, num) for h, w, num in ls], key=lambda x:(-x.h, -x.w))

for i in student:
    print(i.h, i.w, i.num)