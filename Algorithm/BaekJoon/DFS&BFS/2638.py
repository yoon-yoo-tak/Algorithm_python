"""
2638 치즈

"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs():
    q = deque()
    visit = [[False] * m for _ in range(n)]
    q.append((0, 0))
    visit[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] >= 1:
                graph[nx][ny] += 1
            else:
                q.append((nx, ny))
                visit[nx][ny] = True

def is_melt(graph:list):
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                return True
    return False
cnt = 0
while is_melt(graph):
    cnt += 1
    bfs()
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 1:
                graph[i][j] = 1

print(cnt)



