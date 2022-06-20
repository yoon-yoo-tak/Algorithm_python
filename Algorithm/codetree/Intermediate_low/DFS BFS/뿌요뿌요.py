"""
뿌요뿌요
"""
import sys

input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny] != grid[x][y]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny)
        cnt += 1


bbu = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt = 1
            dfs(i, j)
            bbu.append(cnt)
ans = 0
for i in bbu:
    if i >= 4:
        ans += 1
print(ans, max(bbu))