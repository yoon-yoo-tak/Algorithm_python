"""

2178 미로탐색

BFS는 최단거리를 구할 수 있다는 점 활용

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

maze = list(input().strip() for _ in range(n))
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
q.append((0, 0))
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1:
            continue
        if maze[nx][ny] != '1':
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1


print(dist[n - 1][m - 1])