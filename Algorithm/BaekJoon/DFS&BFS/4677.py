"""
4677 - Oil Deposits

1. 아이디어
2. 시간복잡도
3. 자료구조
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
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] == '*':
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    graph = [list(input().strip()) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@' and not visit[i][j]:
                bfs(i, j)
                count += 1

    print(count)
