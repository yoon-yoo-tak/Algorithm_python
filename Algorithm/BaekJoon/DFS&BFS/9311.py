"""
9311 - Robot in Maze

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [input().strip() for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'G':
                q.append((i, j))
                dist[i][j] = 0
            if graph[i][j] == 'S':
                end_x, end_y = i, j
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] != -1:
                continue
            if graph[nx][ny] == 'X':
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    if dist[end_x][end_y] == -1:
        print('No Exit')
    else:
        print('Shortest Path:', dist[end_x][end_y])