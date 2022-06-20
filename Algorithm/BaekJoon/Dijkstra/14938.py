"""
14938 서강그라운드
"""
import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
    q = []
    dist = [int(1e10)] * (n + 1)
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
    return dist



n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = 0
for i in range(1, n + 1):
    temp = dijkstra(i)
    temp_ans = 0
    for j in range(1, n + 1):
        if temp[j] <= m:
            temp_ans += items[j]
    ans = max(ans, temp_ans)

print(ans)