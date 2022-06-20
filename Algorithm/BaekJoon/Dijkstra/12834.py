"""
12834 주간 미팅
"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, v, e = map(int, input().split())
a, b = map(int, input().split())
pos = list(map(int, input().split()))
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))
ans = 0


def dijkstra(start):
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
    return dist


distance_a = dijkstra(a)
distance_b = dijkstra(b)

for p in pos:
    dist_a = -1 if distance_a[p] == INF else distance_a[p]
    dist_b = -1 if distance_b[p] == INF else distance_b[p]
    ans += dist_b + dist_a


print(ans)