"""

1260 DFS와BFS

인접리스트 방식
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)