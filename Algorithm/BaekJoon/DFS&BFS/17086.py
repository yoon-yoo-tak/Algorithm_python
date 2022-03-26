"""

17086 아기 상어 2

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]

def bfs(x, y):
    q = deque()
    # multisource bfs
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
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
            if a[nx][ny] != 0:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

bfs(0, 0)
max_dist = 0
for i in dist:
    for j in i:
        max_dist = max(max_dist, j)

print(max_dist)