"""
16236 아기 상어
"""

import sys
from collections import deque
input = sys.stdin.readline




n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
baby_shark_size = 2
time = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
