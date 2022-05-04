"""
12873 기념품

"""

import sys

input = sys.stdin.readline

n = int(input())

ls = [i for i in range(1, n + 1)]
start = 1
idx = -1
while len(ls) > 1:
    for _ in range(start ** 3):
        idx += 1
        if idx == len(ls):
            idx = 0
    ls.pop(idx)


print(*ls)