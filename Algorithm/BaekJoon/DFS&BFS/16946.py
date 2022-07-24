"""
16946 벽 부수고 이동하기 4

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    a = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        zero_pos[x][y] = cnt
        for dx, dy in dxy:
            nx, ny =  x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            a += 1
    return a



dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zero_pos = [[0] * m for _ in range(n)]
pos_info = dict()
pos_info[0] = 0
cnt = 1

for i in range(n):
    for j in range(m):
        if not graph[i][j] and not visited[i][j]:
            visited[i][j] = True
            a = bfs(i, j)
            pos_info[cnt] = a
            cnt += 1

for i in range(n):
    for j in range(m):
        temp = set()
        if graph[i][j]:
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                temp.add(zero_pos[nx][ny])
            for tmp in temp:
                graph[i][j] += pos_info[tmp]
                graph[i][j] %= 10

for i in graph:
    print(''.join(map(str,i)))