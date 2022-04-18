"""
5427 불
"""
import sys
from collections import deque
input = sys.stdin.readline

tt = int(input())
def bfs():
    while q:
        x, y = q.popleft()
        if dist[x][y] != 'F':
            flag = dist[x][y]
        else:
            flag = 'F'

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and (graph[nx][ny] == '.' or graph[nx][ny] == '@'):
                    if flag == 'F':
                        dist[nx][ny] = flag
                    else:
                        dist[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != 'F':
                    return flag + 1
    return 'IMPOSSIBLE'


for _ in range(tt):
    m, n = map(int, input().split())
    q = deque()
    graph = []
    dist = [[-1] * m for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(n):
        graph.append(list(input().strip()))
        for j in range(m):
            if graph[i][j] == '@':
                dist[i][j] = 0
                start = (i, j)
            elif graph[i][j] == '*':
                dist[i][j] = 'F'
                q.append((i, j))
    q.append(start)
    print(bfs())




