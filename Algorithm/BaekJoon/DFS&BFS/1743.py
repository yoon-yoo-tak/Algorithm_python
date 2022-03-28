"""

1743 음식물 피하기

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

def bfs(x, y):
    count = 0
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        count += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] != 1:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
    return count

c_ls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]:
            c_ls.append(bfs(i, j))

if len(c_ls) == 0:
    print(0)
else:
    print(max(c_ls))