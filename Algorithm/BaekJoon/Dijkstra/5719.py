"""
5719 거의 최단 경로
"""

import sys, heapq
from collections import deque
input = sys.stdin.readline
INF = int(1e10)


def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for i in graph[x]:
            weight = dist_x + graph[x][i]
            if weight < dist[i]:
                dist[i] = weight
                heapq.heappush(q, (weight, i))

def bfs():
    q = deque()
    q.append(d)
    while q:
        x = q.popleft()
        if x == s:
            continue
        for b_x, b_c in graph_b[x]:
            if dist[b_x] + graph[b_x][x] == dist[x]:
                if (b_x, x) not in delete:
                    delete.append((b_x, x))
                    q.append(b_x)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())
    graph = [dict() for _ in range(n)]
    graph_b = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u][v] = p
        graph_b[v].append((u, p))
    dist = [INF] * n
    dijkstra()

    delete = []
    bfs()

    for u, v in delete:
        del graph[u][v]
    dist = [INF] * n
    dijkstra()
    print(-1 if dist[d] == INF else dist[d])