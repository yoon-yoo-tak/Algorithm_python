"""
10026 적록색약

"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]
visit = [[False] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ls = ['R', 'G', 'B']


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] != a[x][y]:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

not_sy = 0
for k in ls:
    for i in range(n):
        for j in range(n):
            if a[i][j] == k and not visit[i][j]:
                bfs(i, j)
                not_sy += 1
print(not_sy, end=' ')
visit = [[False] * n for _ in range(n)]
not_sy = 0
new_a = []
for i in a:
    new_a.append(i.replace('R', 'G'))
new_ls = ['G', 'B']
for k in new_ls:
    for i in range(n):
        for j in range(n):
            if new_a[i][j] == k and not visit[i][j]:
                bfs(i, j)
                not_sy += 1
print(not_sy)

for i in new_a:
    print(i)