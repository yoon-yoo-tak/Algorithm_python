"""

2644 촌수계산

"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x):
    q = deque()
    q.append(x)
    dist[x] = 0
    while q:
        x = q.popleft()
        for y in graph[x]:
            if dist[y] != -1:
                continue
            dist[y] = dist[x] + 1
            q.append(y)

bfs(a)

print(dist[b])

