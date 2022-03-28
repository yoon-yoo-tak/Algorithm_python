"""

7576 토마토

"""
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if a[nx][ny] == -1:
                continue
            if a[nx][ny] != 0:
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

bfs()
ans = 0
max_v = 0
for i in dist:
    ans += i.count(-1)
    max_v = max(max_v, max(i))
ans1 = 0
for j in a:
    ans1 += j.count(-1)
if ans != ans1:
    print(-1)
else:
    print(max_v)
