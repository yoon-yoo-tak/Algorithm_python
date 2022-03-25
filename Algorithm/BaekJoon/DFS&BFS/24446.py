"""

24446 알고리즘 수업 - 너비 우선 탐색 3

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(v):
    q = deque([v])
    dist[v] = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if dist[i] != -1:
                continue
            q.append(i)
            dist[i] = dist[n] + 1

bfs(v)

for i in range(1, len(dist)):
    print(dist[i])


