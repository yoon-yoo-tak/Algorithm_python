"""

3055 탈출

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dist_w = [[-1] * m for _ in range(n)]
dist_h = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs_w():
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                visit[i][j] = True
                q.append((i, j))
                dist_w[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] != '.':
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
            dist_w[nx][ny] = dist_w[x][y] + 1

def bfs_h():
    q = deque()
    for i in range(n):
        for j in range(m):
            visit[i][j] = False
            if a[i][j] == 'S':
                visit[i][j] = True
                q.append((i, j))
                dist_h[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if dist_w[nx][ny] != -1 and dist_w[nx][ny] <= dist_h[x][y] + 1:
                continue
            if a[nx][ny] != '.' and a[nx][ny] != 'D':
                continue
            visit[nx][ny] = True
            q.append((nx, ny))
            dist_h[nx][ny] = dist_h[x][y] + 1


bfs_w()
bfs_h()

for i in range(n):
    for j in range(m):
        if a[i][j] == 'D':
            if dist_h[i][j] == -1:
                print("KAKTUS")
            else:
                print(dist_h[i][j])




