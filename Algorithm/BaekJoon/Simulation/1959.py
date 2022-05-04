"""
1959 달팽이 3
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
idx = 0
cnt = 0
x, y = 0, 0
graph[0][0] = 1
while True:
    if idx == 4:
        idx = 0
    nx, ny = x + dx[idx], y + dy[idx]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        idx += 1
        cnt += 1
        continue
    if graph[nx][ny] != 0:
        idx += 1
        cnt += 1
        continue
    graph[nx][ny] = graph[x][y] + 1
    x, y = nx, ny
    if graph[nx][ny] == n * m:
        break
print(cnt)
for i in range(n):
    for j in range(m):
        if graph[i][j] == m * n:
            ax, ay = i + 1, j + 1
print(ax, ay)