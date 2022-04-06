"""
6229 - Bronze Lilypad Pond

0 - 물
1 - 발판
2 - 바위
3 - 시작점
4 - 목표점
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, m1, m2 = map(int, input().split())

grpah = [list(map(int, input().split())) for _ in range(n)]
dxy = [(m1, m2), (-m1, m2), (m1, -m2), (-m1, -m2), (m2, m1), (-m2, m1), (m2, -m1), (-m2, -m1)]
dist = [[-1] * m for _ in range(n)]

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
            if grpah[nx][ny] == 0 or grpah[nx][ny] == 2:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

for i in range(n):
    for j in range(m):
        if grpah[i][j] == 3:
            bfs(i, j)
        if grpah[i][j] == 4:
            end_x, end_y = i, j

print(dist[end_x][end_y])