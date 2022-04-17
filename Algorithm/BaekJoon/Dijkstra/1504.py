"""
1504 특정한 최단 경로
"""
import sys, heapq
INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
one = dijkstra(1)
v1, v2 = map(int, input().split())
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
ans = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(ans if ans < INF else -1)