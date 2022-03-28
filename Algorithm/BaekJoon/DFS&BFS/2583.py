"""

2583 영역 구하기

"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
            cnt += 1

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(k):
    x, y, a, b = map(int, input().split())
    for i in range(y, b):
        for j in range(x, a):
            graph[i][j] = 1

cnt = 1
all = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visit[i][j]:
            cnt = 1
            bfs(i, j)
            all.append(cnt)
all.sort()
print(len(all))
print(*all)

