"""
갈 수 있는 곳들
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int ,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

q = deque()
for _ in range(k):
    a, b = map(lambda x: x- 1, map(int, input().split()))
    q.append((a, b))
    visited[a][b] = True
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny]:
            continue
        q.append((nx, ny))
        visited[nx][ny] = True

ans = 0
for i in visited:
    ans += i.count(True)
print(ans)