"""
14221 편의점
"""
import sys, heapq
from collections import defaultdict
INF = int(1e10)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

p, q = map(int, input().split())
house = list(map(int, input().split()))
convi = list(map(int, input().split()))

dist = [INF] * (n + 1)
min_dist, ans = INF, 0

for c in convi:
    pq = [(0, c)]
    min_dists = [INF] * (n + 1)
    min_dists[c] = 0
    while pq:
        dist_x, x = heapq.heappop(pq)

        if x in house:
            break
        if dist[x] != dist_x:
            continue
        for uu, weight in graph[x]:
            alt = dist_x + weight
            if min_dists[uu] > alt and uu != convi:
                min_dists[uu] = alt
                heapq.heappush(pq, (alt, uu))
            dist[uu] = min(dist[uu], min_dists[uu])
for h in house:
    if min_dist > dist[h]:
        min_dist = dist[h]
        ans = h
print(ans)
