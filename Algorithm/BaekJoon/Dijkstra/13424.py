"""
13424 비밀 모임
"""
import sys, heapq
INF = int(1e11)
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (n + 1)
    dist[start] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for uu, weight in graph[x]:
            if dist[uu] > weight + dist[x]:
                dist[uu] = weight + dist[x]
                heapq.heappush(q, (dist[uu], uu))
    return dist


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    k = int(input()) # 친구 수
    friend_pos = list(map(int, input().split())) # 친구 위치

    total_dist = [INF] * (n + 1)
    for i in range(1, n + 1):
        temp = dijkstra(i)
        total_dist[i] = sum(temp[j] for j in friend_pos)
    print(total_dist.index(min(total_dist)))