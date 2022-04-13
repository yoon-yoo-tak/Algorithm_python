"""
6004 The Chivalrous Cow
"""
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
dxy = [(-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, -2)]
dist = [[-1] * m for _ in range(n)]
graph = [input().strip() for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'K':
           q.append((i, j))
           dist[i][j] = 0
        if graph[i][j] == 'H':
            endx, endy = i, j
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == '*':
            continue
        if dist[nx][ny] != -1:
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[endx][endy])