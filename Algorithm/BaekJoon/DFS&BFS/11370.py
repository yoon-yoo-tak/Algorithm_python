"""
11370 - Spawn of Ungoliant

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(input().strip()) for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visit = [[False] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'S':
                q.append((i, j))
                visit[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '.':
                continue
            if visit[nx][ny]:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if visit[i][j]:
                graph[i][j] = 'S'

    for i in graph:
        print(''.join(i))