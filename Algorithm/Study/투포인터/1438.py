"""
1438 가장 작은 직사각형
"""
import sys

input = sys.stdin.readline

n = int(input())
xy, x, y = [], [], []
for _ in range(n):
   a, b = map(int, input().split())
   xy.append([a, b])
   x.append(a)
   y.append(b)
x.sort()
y.sort()
min_x = x[0] - 1
max_x = x[-1] + 1
min_y = y[0] - 1
max_y = y[-1] + 1
l = min_x
r = min_y


