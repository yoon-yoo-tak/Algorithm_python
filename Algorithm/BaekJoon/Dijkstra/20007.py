"""
20007 떡 돌리기
"""
import sys, heapq

input = sys.stdin.readline


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for u, weight in graph[x]:
            if dist[u] > dist[x] + weight:
                dist[u] = dist[x] + weight
                heapq.heappush(q, (dist[u], u))

n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
dist = [int(1e10)] * n

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(y)

for i in range(n):
    if dist[i] > x // 2:
        print(-1)
        sys.exit()

dist.sort()
day_dist = 0
day = 1
for i in range(n):
    if (day_dist + dist[i]) * 2 <= x:
        day_dist += dist[i]
    else:
        day_dist = dist[i]
        day += 1
print(day)
