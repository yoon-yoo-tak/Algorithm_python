"""
안전 지대
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
vill = [list(map(int, input().split())) for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
height = 0
for i in range(n):
    for j in range(m):
        height = max(height, vill[i][j])


def dfs(x, y, h):
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        if vill[nx][ny] <= h:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, h)

ans = [0] * (height + 1)
for i in range(1, height + 1):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if vill[x][y] > i and not visited[x][y]:
                cnt += 1
                dfs(x, y, i)
    ans[i] = cnt
ans2 = max(ans)
ans1 = ans.index(ans2)
if ans1 == 0:
    ans1 = 1
print(ans1, ans2)

