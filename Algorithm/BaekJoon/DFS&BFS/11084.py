"""
11084 나이트의 염탐

"""

import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 2), (-1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]
MOD = 1000000009

visited = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
count = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
count[1][1] = 1
visited[1][1] = 0
q = deque()
q.append((1, 1, 0))

while q:
    x, y, d = q.popleft()
    for dx, dy in dxy:
        nx, ny, nd = x + dx, y + dy, d + 1

        if nx <= 0 or ny <= 0 or nx > n or ny > m:
            continue
        if  nd < visited[nx][ny]:
            count[nx][ny] = count[x][y]
            visited[nx][ny] = nd
            q.append((nx, ny, nd))
        elif nd == visited[nx][ny]:
            count[nx][ny] = (count[nx][ny] + count[x][y]) % MOD

if visited[n][m] != float('inf'):
    print(visited[n][m], count[n][m])
else:
    print('None')


