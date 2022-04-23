"""
5972 택배 배송
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
dist[1] = 0
heapq.heappush(q, (0, 1))
while q:
    dist_x, x = heapq.heappop(q)
    if dist[x] != dist_x:
        continue
    for uu, weight in graph[x]:
        if dist[uu] > dist[x] + weight:
            dist[uu] = dist[x] + weight
            heapq.heappush(q, (dist[uu], uu))

print(dist[n])