"""

2589 보물섬

"""

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] != -1:
                continue
            if graph[nx][ny] == 'W':
                continue
            q.append((nx ,ny))
            dist[nx][ny] = dist[x][y] + 1
max_len = -1
for i in range(n):
    for j in range(m):
        dist = [[-1] * m for _ in range(n)]
        if graph[i][j] == 'L' and dist[i][j] == -1:
            bfs(i, j)
            for k in dist:
                max_len = max(max_len, max(k))

print(max_len)