"""
9140 Přeprava materiálu
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

while True:
    n, m, start, end = map(int, input().split())
    if n == m == start == end == 0:
        break
    graph = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = []
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
    print(dist[end])
