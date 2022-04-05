"""
이코테 DFS/BFS 파트 연습 문제 - 미로 탈출

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import  deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = [[-1] * m for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if dist[nx][nx] != -1:
                continue
            if graph[nx][ny] == '0':
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1



bfs(0, 0)
print(dist[n - 1][m - 1])
print(dist)


"""
5 6
101010
111111
000001
111111
111111
"""