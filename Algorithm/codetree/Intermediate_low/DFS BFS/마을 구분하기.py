"""
마을 구분하기
"""
import sys

input = sys.stdin.readline

village = []

n = int(input())
town = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or town[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global cnt
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            cnt += 1
            visited[nx][ny] = True
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if town[i][j] != 0 and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            village.append(cnt)

print(len(village))
for i in sorted(village):
    print(i)