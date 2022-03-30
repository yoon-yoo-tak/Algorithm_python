"""

14496 그대, 그머가 되어

"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0
    while q:
        node = q.popleft()
        for i in graph[node]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[node] + 1

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dist = [-1] * (n + 1)

bfs(a)
print(dist[b])




