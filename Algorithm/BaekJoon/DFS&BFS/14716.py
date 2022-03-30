"""

14716 현수막

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
count = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and not visit[i][j]:
            bfs(i, j)
            count += 1

print(count)