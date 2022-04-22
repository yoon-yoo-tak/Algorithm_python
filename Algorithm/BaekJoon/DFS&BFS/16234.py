"""
16234 인구이동
"""
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    temp = []  # 연합 좌표 저장
    temp.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if abs(graph[x][y] - graph[nx][ny]) < l or abs(graph[x][y] - graph[nx][ny]) > r:
                continue
            q.append((nx, ny))
            temp.append([nx, ny])
            visited[nx][ny] = True
    return temp


cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    flag = True
                    population = sum([graph[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        graph[x][y] = population
    if not flag:
        break
    cnt += 1

print(cnt)


