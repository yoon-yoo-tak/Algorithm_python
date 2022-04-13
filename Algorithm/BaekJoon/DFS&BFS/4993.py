"""
4993 Red and Black
"""
import sys
from collections import deque
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [input().strip() for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cnt = 1
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                q.append((i, j))
                visit[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] != '.':
                continue
            q.append((nx, ny))
            cnt += 1
            visit[nx][ny] = True

    print(cnt)