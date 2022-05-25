import sys
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        if ls[x][y] in ['3','4','5']:
            print('TAK')
            print(dist[x][y])
            return
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] != -1:
                continue
            if ls[nx][ny] == '1':
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

    print('NIE')


n, m = map(int, input().split())
ls = [list(input().strip()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(n):
    for j in range(m):
        if ls[i][j] == '2':
            a, b = i, j

bfs(a, b)
