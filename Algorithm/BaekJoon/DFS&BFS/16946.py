"""
16946 벽 부수고 이동하기 4

"""

import sys
from collections import deque

def bfs(x, y):
    cnt = 0
    q = deque()
    visit = [[False] * m for _ in range(n)]
    q.append((x, y))
    visit[x][y] = True
    while q:
        cnt += 1
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and graph[nx][ny] == '0':
                q.append((nx, ny))
                visit[nx][ny] = True
    return cnt
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            graph[i][j] = '0'
            graph[i][j] = str(bfs(i, j))

for i in graph:
    print(''.join(i))