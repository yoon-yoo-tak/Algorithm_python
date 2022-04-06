"""
17198 - Bucket Brigade

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

graph = [input().strip() for _ in range(10)]
dist = [[-1] * 10 for _ in range(10)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
                continue
            if dist[nx][ny] != -1:
                continue
            if graph[nx][ny] == 'R':
                continue
            if graph[nx][ny] == 'B':
                return dist[x][y]
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1


for i in range(10):
    for j in range(10):
        if graph[i][j] == 'L':
            print(bfs(i, j))
