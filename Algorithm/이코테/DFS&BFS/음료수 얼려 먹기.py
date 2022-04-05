"""
이코테 DFS/BFS 파트 연습 문제 - 음료수 얼려 먹기

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visit = [[False] * m for _ in range(n)]
cnt = 0
def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == '1':
            continue
        if visit[nx][ny]:
            continue
        dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and  not visit[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)
print(visit)