"""
14442 벽 부수고 이동하기 2
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(x, y, wall):
    q = deque()
    q.append((x, y, wall))
    dist[x][y][wall] = 1
    while q:
        x, y, wall = q.popleft()
        if x == n - 1 and y == m - 1:
            return dist[n - 1][m - 1][wall]
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0 and dist[nx][ny][wall] == 0:
                q.append((nx, ny, wall))
                dist[nx][ny][wall] = dist[x][y][wall] + 1
            if graph[nx][ny] == 1 and wall < k:
                q.append((nx, ny, wall + 1))
                dist[nx][ny][wall + 1] = dist[x][y][wall] + 1

    return -1

print(bfs(0, 0, 0))
