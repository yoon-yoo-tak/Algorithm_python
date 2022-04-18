"""
1753 최단경로
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, V, weight = map(int, input().split())
    graph[u].append((V, weight))
dist = [INF] * (v + 1)
dist[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    dist_x, x = heapq.heappop(q)
    if dist[x] != dist_x:
        continue
    for uu, weight in graph[x]:
        if dist[uu] > dist[x] + weight:
            dist[uu] = dist[x] + weight
            heapq.heappush(q, (dist[uu], uu))

for i in dist[1:]:
    print(i if i != INF else 'INF')
