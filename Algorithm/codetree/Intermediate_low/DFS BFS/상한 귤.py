"""
상한 귤
0 빈칸
1 귤
2 상한 귤
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * n for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            q.append((i, j))
            dist[i][j] = 0

while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if dist[nx][ny] != -1:
            continue
        if board[nx][ny] != 1:
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and dist[i][j] == -1:
            dist[i][j] = -2

for i in dist:
    print(*i)
