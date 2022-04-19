"""
10163 색종이
"""

import sys

input = sys.stdin.readline
ls = [[0] * 1001 for _ in range(1001)]
n = int(input())
for i in range(1, n + 1):
    y, x, w, h = map(int, input().split())
    for j in range(x, x + h):
        for k in range(y, y + w):
            ls[j][k] = i
temp = [0] * (n + 1)
for k in range(1, n + 1):
    for i in range(1001):
        for j in range(1001):
            if ls[i][j] == k:
                temp[k] += 1
for i in temp[1:]:
    print(i)

