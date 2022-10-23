"""
18402 RUN
"""
import sys, heapq
INF = int(1e9)
input = sys.stdin.readline


def dijkstra(start, end):
    q = []
    dist = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist_x != dist[x]:
            continue
        for u, weight in graph[x]:
            if dist[u] > dist[x] + weight:
                dist[u] = dist[x] + weight
                heapq.heappush(q, (dist[u], u))
    return dist[end]


n = int(input())
e = int(input())
t = int(input())
m = int(input())
ans = 0
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n + 1):
    if dijkstra(i, e) <= t:
        ans += 1

print(ans)