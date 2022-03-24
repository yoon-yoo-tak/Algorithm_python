"""

5567 결혼식

거리가 1, 2인 친구만 초대
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
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
print(dist.count(1) + dist.count(2))