"""
숨바꼭질 BFS로 풀어보기
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

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

bfs(1)
max_val = max(dist)
print(dist.index(max_val), dist[dist.index(max_val)], dist.count(max_val))