"""

1012 유기농 배추

"""
import sys
input = sys.stdin.readline
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    visit[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if visit[nx][ny]:
            continue
        if a[nx][ny] == 0:
            continue
        dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    a = [[0] * n for _ in range(m)]
    cnt = 0
    worm = []
    visit = [[False] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        a[x][y] = 1
    for i in range(m):
        for j in range(n):
            if a[i][j] == 0 or visit[i][j]:
                continue
            dfs(i,j)
            worm.append(cnt)
    print(len(worm))

