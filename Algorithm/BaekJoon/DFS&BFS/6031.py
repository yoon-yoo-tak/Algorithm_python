"""
6031 Feeding Time
"""
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [input().strip() for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
visit = [[False] * m for _ in range(n)]
max_cnt = -1
def bfs(x, y):
    cnt = 1
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
            if graph[nx][ny] == '*':
                continue
            cnt += 1
            q.append((nx, ny))
            visit[nx][ny] = True
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == '.' and not visit[i][j]:
            max_cnt = max(max_cnt, bfs(i, j))

print(max_cnt)