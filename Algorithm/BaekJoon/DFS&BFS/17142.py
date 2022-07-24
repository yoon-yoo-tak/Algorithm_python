"""
17142 연구소 3
"""
import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph, temp = [], []
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(n):
        if ls[j] == 2:
            temp.append((i, j, 0))
    graph.append(ls)


def check(graph):
    for i in range(n):
        for j in range(n):
            if not graph[i][j]:
                return -1
    return 0

def bfs(tmp, graph):
    visited = [[False] * n for _ in range(n)]
    graph = deepcopy(graph)
    q = deque()
    q.extend(tmp)
    last = 0
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        for dx, dy in dxy:
            nx, ny = x + dx , y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    last = cnt + 1
                q.append((nx, ny, cnt + 1))
    chk = check(graph)
    if chk == 0:
        return last
    else:
        return -1


ans = int(1e10)

for val in list(combinations(temp, m)):
    res = bfs(val, graph)
    if ans > res != -1:
        ans = res

print(-1 if ans == int(1e10) else ans)



