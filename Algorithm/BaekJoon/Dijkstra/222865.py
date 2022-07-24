"""
22865 가장 먼 곳
"""
import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [int(1e10)] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for u, weight in graph[x]:
            if dist[u] > dist[x] + weight:
                dist[u] = dist[x] + weight
                heapq.heappush(q, (dist[u], u))
    return dist


n = int(input())
a, b, c = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))

dist_a = dijkstra(a)
dist_b = dijkstra(b)
dist_c = dijkstra(c)
ans = 0
mx_dist = 0
for i in range(1, n + 1):
    if mx_dist < min(dist_c[i], dist_b[i] , dist_a[i]):
        mx_dist = min(dist_c[i], dist_b[i] , dist_a[i])
        ans = i

print(ans)