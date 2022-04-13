"""
6798 Knight Hop
"""
import sys
from collections import deque
input = sys.stdin.readline

b, a = map(int, input().split())
a = 8 - a
b -= 1
d, c = map(int ,input().split())
c = 8 - c
d -= 1
dxy = [(-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, -2)]
dist = [[-1] * 8 for _ in range(8)]
q = deque()
q.append((a, b))
dist[a][b] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue
        if dist[nx][ny] != -1:
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[c][d])
