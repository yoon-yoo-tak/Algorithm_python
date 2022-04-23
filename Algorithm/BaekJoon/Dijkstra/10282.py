"""
10282 해킹
"""
import sys, heapq
INF = int(1e10)
input = sys.stdin.readline

t = int(input())
for tt in range(t):
    n, d, start = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)
    for _ in range(d):
        b, a, c = map(int, input().split())
        graph[a].append((b, c))
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for uu, weight in graph[x]:
            if dist[uu] > dist[x] + weight:
                dist[uu] = dist[x] + weight
                heapq.heappush(q, (dist[uu], uu))
    temp = [i for i in dist[1:] if i < INF]
    cnt = len(temp)
    time = max(temp)
    print(cnt, time)



