"""
2146 다리 만들기

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
def bfs1(x, y):
    global count
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    graph[x][y] = count
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] != 1:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
            graph[nx][ny] = count

def bfs2(v):
    global min_dist
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > 0 and graph[nx][ny] != v:
                min_dist = min(min_dist, dist[x][y])
                return
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
count = 1
min_dist = 200

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visit[i][j]:
            bfs1(i, j)
            count += 1

for i in range(1, count):
    bfs2(i)

print(min_dist)