"""
17129 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [[-1] * m for _ in range(n)]
a = [input().strip() for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny] == '1':
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
            if a[nx][ny] in ('3', '4', '5'):
                print('TAK')
                print(dist[nx][ny])
                exit()
    print('NIE')

for i in range(n):
    for j in range(m):
        if a[i][j] == '2':
            bfs(i, j)