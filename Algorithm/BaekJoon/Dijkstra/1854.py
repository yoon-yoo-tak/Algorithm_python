"""
1854 k번째 최단경로 찾기
"""
import sys, heapq
INF = int(2e10)
input = sys.stdin.readline

def dijkstra(v):
    heapq.heappush(q, (0, v))
    dist[v][0] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        for uu, weight in graph[x]:
            if dist_x + weight < dist[uu][k - 1]:
                dist[uu][k - 1] = dist_x + weight
                dist[uu].sort()
                heapq.heappush(q, (dist_x + weight, uu))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [[INF] * k for _ in range(n + 1)]
q = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

dijkstra(1)

for i in range(1, n + 1):
    print(-1 if dist[i][k - 1] == INF else dist[i][k - 1])