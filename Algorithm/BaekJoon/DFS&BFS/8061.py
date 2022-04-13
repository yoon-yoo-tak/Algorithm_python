"""
8061 Bitmap
"""
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            q.append((i, j))
            dist[i][j] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1:
            continue
        if graph[nx][ny] == '1':
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

for i in dist:
    print(*i)

