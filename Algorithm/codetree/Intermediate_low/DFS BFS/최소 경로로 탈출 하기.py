"""
최소 경로로 탈출 하기
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = [[-1] * m for _ in range(n)]
q = deque()
q.append((0, 0))
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] != 1:
            continue
        if dist[nx][ny] != -1:
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[n - 1][m - 1])