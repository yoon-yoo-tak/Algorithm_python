"""
o : 양
v : 늑대
# : 벽
. : 땅
양 > 늑대 : win
양 <= 늑대 : dead
"""

from collections import deque

n, m = map(int, input().split())
farm = [list(input()) for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sheep_cnt, wolf_cnt, sheep, wolf = 0, 0, 0, 0

visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    global sheep, wolf
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        if farm[x][y] == 'v':
            wolf += 1
        if farm[x][y] == 'o':
            sheep += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if farm[nx][ny] == '#':
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if farm[i][j] != '#' and not visited[i][j]:
            sheep, wolf = 0, 0
            bfs(i, j)
            if sheep > wolf:
                sheep_cnt += sheep
            else:
                wolf_cnt += wolf

print(sheep_cnt, wolf_cnt)


