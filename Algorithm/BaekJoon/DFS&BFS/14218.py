"""

14218 그래프 탐색 2

"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if dist[i] != -1:
                continue
            q.append(i)
            dist[i] = dist[x] + 1

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    bfs(1)
    print(*dist[1:])
    dist = [-1] * (n + 1)