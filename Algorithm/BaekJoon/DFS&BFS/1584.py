"""
1584 게임
"""

import sys
from collections import deque
input = sys.stdin.readline

graph = [[0] * 501 for _ in range(501)]
dist = [[-1] * 501 for _ in range(501)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
if n > 0:
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            graph[i][j] = 1
m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
if m > 0:
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            graph[i][j] = 2

# 위험구역 1 죽음구역 2

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 501 or ny < 0 or ny >= 501:
                continue
            if dist[nx][ny] != -1:
                continue
            if graph[nx][ny] == 0:
                q.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]
            elif graph[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

bfs(0, 0)
print(dist[500][500])