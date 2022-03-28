"""

토마토(3차원버전)

"""
import sys
from collections import deque

m, n, h = map(int, input().split())
graph = []
q = deque([])

for i in range(h):
    ls = []
    for j in range(n):
        ls.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if ls[j][k] == 1:
                q.append([i, j, k])
    graph.append(ls)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while (q):
    x, y, z = q.popleft()

    for i in range(6):
        a = x + dx[i]
        b = y + dy[i]
        c = z + dz[i]
        if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
            q.append([a, b, c])
            graph[a][b][c] = graph[x][y][z] + 1

ans = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans - 1)