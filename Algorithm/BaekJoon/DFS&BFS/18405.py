"""

18405 경쟁적 전염

"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
num = [[-1] * n for _ in range(n)]
second = [[-1] * n for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
s, x, y = map(int, input().split())

def bfs():
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

bfs()
for i in graph:
    print(i)