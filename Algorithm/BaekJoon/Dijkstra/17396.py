"""
17396 백도어
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e11)
n, m = map(int, input().split())
ward = list(map(int, input().split()))
graph = [[] for _ in range(n)]
dist = [INF] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
q = []
heapq.heappush(q, (0, 0))
dist[0] = 0
while q:
    dist_x, x = heapq.heappop(q)
    if dist[x] != dist_x:
        continue
    for uu, weight in graph[x]:
        if uu == n - 1 or not ward[uu]:
            if dist[uu] > dist[x] + weight:
                dist[uu] = dist[x] + weight
                heapq.heappush(q, (dist[uu], uu))

print(-1 if dist[n - 1] == INF else dist[n - 1])