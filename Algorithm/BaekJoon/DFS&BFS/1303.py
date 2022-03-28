"""

1303 전투

"""
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
a = [input().strip() for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
w = []
b = []


def bfs(x, y, target):
    count = 1
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
            if a[nx][ny] != target:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
            count += 1
    return count

for i in range(n):
    for j in range(m):
        if a[i][j] == 'W' and not visit[i][j]:
            w.append(bfs(i, j, 'W') ** 2)
        elif a[i][j] == 'B' and not visit[i][j]:
            b.append(bfs(i, j, 'B') ** 2)

print(sum(w), sum(b))
