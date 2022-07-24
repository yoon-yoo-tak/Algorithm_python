"""
18223 민준이와 마산 그리고 건우
"""
import sys,heapq

input = sys.stdin.readline


def dijkstra(start):
    q = []
    dist = [int(1e9)] * (v + 1)
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
    return dist

v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1 > 마산 == 1 > 건우 > 마산 : ok
# else: bad
from_one = dijkstra(1)
from_p = dijkstra(p)
if from_one[v] == (from_one[p] + from_p[v]):
    print('SAVE HIM')
else:
    print('GOOD BYE')