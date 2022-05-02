"""
23563 벽 타기

"""

import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            sx, sy = i, j
        if graph[i][j] == 'E':
            ex, ey = i, j


def is_wall(a, b):  # 벽이랑 인접한 곳인가
    for dx, dy in dxy:
        na, nb = a + dx, b + dy
        if graph[na][nb] == '#':
            return True
    return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:# 범위초과 무시
                continue
            if graph[nx][ny] == '#':                  # 벽 무시
                continue
            if dist[nx][ny] != -1:                    # 방문한곳 무시
                continue

            if is_wall(x, y):                         # 현재 위치가 벽이랑 인접하고
                if is_wall(nx, ny):                   # 다음 위치도 벽이랑 인접하면
                    q.appendleft((nx, ny))            # 벽인곳 먼저 가면서
                    dist[nx][ny] = dist[x][y]         # 시간 유지
                else:                                 # 다음 위치가 벽이랑 인접하지 않으면
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1     # 시간 추가
            else:                                     # 현재 위치가 벽이랑 인접하지 않고
                if is_wall(nx, ny):                   # 다음 위치가 벽이랑 인접하면
                    q.append((nx, ny))                # 벽인곳 먼저 가면서
                    dist[nx][ny] = dist[x][y] + 1     # 시간 추가
                else:
                    q.append((nx, ny))                # 이동하면서
                    dist[nx][ny] = dist[x][y] + 1     # 시간추가


bfs(sx, sy)
print(dist[ex][ey])