"""
14217 그래프 탐색

수도는 1번
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
            if dist[i] != -1:
               continue
            q.append(i)
            dist[i] = dist[node] + 1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())

for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        graph[b].append(c)
        graph[c].append(b)
    else:
        graph[c].remove(b)
        graph[b].remove(c)
    bfs(1)
    print(*dist[1:])
    dist = [-1] * (n + 1)

