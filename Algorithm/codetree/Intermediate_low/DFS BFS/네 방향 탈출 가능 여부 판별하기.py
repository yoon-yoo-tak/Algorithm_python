"""
네 방향 탈출 가능 여부 판별하기
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * m for _ in range(n)]
q = deque()
q.append((0 ,0))
visited[0][0] = True
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny] == 0:
            continue
        q.append((nx, ny))
        visited[nx][ny] = True


print(1 if visited[n - 1][m - 1] else 0)