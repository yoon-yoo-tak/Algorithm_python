"""

18404 현명한 나이트

n X n 체스판
m개의 적에 대해 각각 도달할 수 있는 최소 횟수 출력
나이트의 위치 x, y
적 위치 a, b
"""
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
x, y = map(int, input().split())

dxy = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
dist = [[-1] * (n + 1) for _ in range(n + 1)]


def bfs(c, d):
    q = deque()
    q.append((c, d))
    dist[c][d] = 0
    while q:
        px, py = q.popleft()
        for dx,dy in dxy:
            nx = px + dx
            ny = py + dy
            if nx < 0 or nx >= (n + 1) or ny < 0 or ny >= (n + 1):
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[px][py] + 1
bfs(x, y)
for _ in range(m):
    a, b = map(int, input().split())
    print(dist[a][b], end=' ')