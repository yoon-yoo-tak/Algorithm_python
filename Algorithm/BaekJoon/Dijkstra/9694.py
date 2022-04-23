"""
9694 무엇을 아느냐가 아니라 누구를 아느냐가 문제다
"""
import sys, heapq
INF = int(1e9)
input = sys.stdin.readline

t = int(input())

for tt in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(m)]
    dist = [INF] * m
    for _ in range(n):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = []
    heapq.heappush(q, (0, 0))
    dist[0] = 0
    ans = [-1 for _ in range(m)]
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for uu, weight in graph[x]:
            if dist[uu] > dist[x] + weight:
                ans[uu] = x
                dist[uu] = dist[x] + weight
                heapq.heappush(q, (dist[uu], uu))

    result = [m - 1]
    idx = m - 1
    while ans[idx] != -1:
        idx = ans[idx]
        result.append(idx)
    result.reverse()
    if len(result) == 1:
        result = [-1]
    print(f'Case #{tt}:', *result)