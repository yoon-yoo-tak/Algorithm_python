"""

3187 양치기 꿍

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visit = [[False] * m for _ in range(n)]

def bfs(x, y):
    global sheep, wolf
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    wolf, sheep = 0, 0
    while q:
        x, y = q.popleft()
        if a[x][y] == 'k':
            sheep += 1
        if a[x][y] == 'v':
            wolf += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] == '#':
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return [wolf, sheep]

sheep_total, wolf_total = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] != '#' and not visit[i][j]:
            wolf, sheep = bfs(i, j)
            sheep_total += sheep
            wolf_total += wolf

print(sheep_total, wolf_total)