"""

7562 나이트의 이동

"""
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a, b = map(int, input().split()) # 현재위치
    tx, ty = map(int, input().split()) # 목표

    dist = [[-1] * n for _ in range(n)] # 거리배열
    dxy = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    q = deque()
    q.append((a, b))
    dist[a][b] = 0  # 거리배열 > 현재위치 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    print(dist[tx][ty])