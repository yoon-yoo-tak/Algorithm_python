"""
14284 간선 이어가기2
"""
import sys, heapq
INF = int(1e12)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())
q = []
heapq.heappush(q, (0, start))
dist[start] = 0

while q:
    dist_x, x = heapq.heappop(q)
    if dist[x] != dist_x:
        continue
    for uu, weight in graph[x]:
        if dist[uu] > dist[x] + weight:
            dist[uu] = dist[x] + weight
            heapq.heappush(q, (dist[uu], uu))

print(dist[end])

