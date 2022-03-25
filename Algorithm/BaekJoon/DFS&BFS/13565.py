"""

13565 침투

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

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
            if a[nx][ny] != '0':
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

for i in range(m):
    if a[0][i] == '0' and not visit[0][i]:
        bfs(0, i)

print('YES' if visit[n-1].count(True) > 0 else 'NO')

