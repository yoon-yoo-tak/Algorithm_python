"""
5958 Space Exploration
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ls = [input().strip() for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1 , 0), (0, -1)]
visit = [[False] * n for _ in range(n)]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if ls[nx][ny] == '.':
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
ans = 0
for i in range(n):
    for j in range(n):
        if ls[i][j] == '*' and not visit[i][j]:
            bfs(i, j)
            ans += 1

print(ans)