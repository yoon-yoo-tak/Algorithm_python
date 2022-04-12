"""
2573 빙산

"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

year = 0
flag = False

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visit = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visit[i][j]:
                ans.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(ans) == 0:
        break
    if len(ans) >= 2:
        flag = True
        break
    year += 1

print(year if flag else 0)