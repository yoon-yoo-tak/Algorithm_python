"""
14497 주난의 난
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()
q.append((x1 - 1, y1 - 1))
dist[x1 - 1][y1 - 1] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1:
            continue
        if graph[nx][ny] == '1' or graph[nx][ny] == '#':
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
        elif graph[nx][ny] =='0':
            dist[nx][ny] = dist[x][y]
            q.appendleft((nx, ny))

print(dist[x2 - 1][y2 - 1])
