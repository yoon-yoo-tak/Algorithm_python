"""

17204 죽음의 게임

"""
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

graph = [[] for _ in range(n)]
dist = [-1] * n

for i in range(n):
    a = int(input())
    graph[i].append(a)

def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if dist[i] != -1:
                continue
            q.append(i)
            dist[i] = dist[n] + 1

bfs(0)
print(dist[k])