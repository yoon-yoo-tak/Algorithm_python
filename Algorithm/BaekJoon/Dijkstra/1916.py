"""

1916 최소비용 구하기

"""
import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [int(1e9)] * (n + 1)

for _ in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))

start, end = map(int, input().split())

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

print(dist[end])


