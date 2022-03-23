"""

4963 섬의 개수

"""
import sys
input = sys.stdin.readline

dyx = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]

def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dyx:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if a[nx][ny] == 0:
            continue
        if visit[nx][ny]:
            continue
        dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] or a[i][j] == 0:
                continue
            dfs(i, j)
            cnt += 1
    print(cnt)


