"""
5590 船旅
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    q = []
    dist = [INF] * (n + 1)
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist_x, x = heapq.heappop(q)
        if dist_x != dist[x]:
            continue
        for u, weight in graph[x]:
            if dist[u] > dist[x] + weight:
                dist[u] = dist[x] + weight
                heapq.heappush(q, (dist[u], u))
    return dist[end] if dist[end] != INF else -1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, *b = map(int, input().split())
    if a:
        graph[b[0]].append((b[1], b[2]))
        graph[b[1]].append((b[0], b[2]))
    else:
        print(dijkstra(b[0], b[1]))