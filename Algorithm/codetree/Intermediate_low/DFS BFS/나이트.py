"""
나이트
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(lambda x: x - 1, map(int, input().split()))
dist = [[-1] * n for _ in range(n)]
dxy = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
q = deque()
q.append((r1, c1))
dist[r1][c1] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if dist[nx][ny] != -1:
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[r2][c2])