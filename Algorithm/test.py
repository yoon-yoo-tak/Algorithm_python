"""
16973 직사각형 탈출
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and 0 <= nx + h - 1 < n and 0 <= ny + w - 1 < m:
                if dist[nx][ny] == -1:
                    if isOk(nx, ny):
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

def isOk(x, y):
    for xWall, yWall in wall:
        if x <= xWall < x + h and y <= yWall < y + w:
            return False
    return True

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
h, w, sx, sy, ex, ey = map(int, input().split())
dist = [[-1] * m for _ in range(n)]
wall = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 1]

bfs(sx - 1, sy - 1)
print(dist[ex - 1][ey - 1])



