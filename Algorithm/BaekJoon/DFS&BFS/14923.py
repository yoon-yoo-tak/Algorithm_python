"""
14923 미로 탈출

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[[-1, -1] for _ in range(m)] for _ in range(n)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs():
    q = deque()
    q.append((hx-1, hy-1, 0))
    dist[hx-1][hy-1][0] = 0
    while q:
        x, y, z = q.popleft()
        if x == ex-1 and y == ey-1:
            return dist[x][y][z]
        for i in range(4):
            nx, ny, nz = x+dx[i], y+dy[i], z
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny]:
                if nz:
                    continue
                else:
                    nz = 1
            if dist[nx][ny][nz] == -1:
                dist[nx][ny][nz] = dist[x][y][z]+1
                q.append((nx, ny, nz))
    return -1

print(bfs())
