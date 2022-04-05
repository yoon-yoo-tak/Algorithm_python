"""
이코테 구현파트 연습문제 1

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
n = int(input())
dxy = dict()
dxy['L'] = (0, -1)
dxy['R'] = (0, 1)
dxy['U'] = (-1, 0)
dxy['D'] = (1, 0)

plan = input().split()
start = [1, 1]
x, y = start
for p in plan:
    nx, ny = x + dxy[p][0], y + dxy[p][1]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)