"""

1916 최소비용 구하기

"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
con = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, weight = map(int, input().split())
    con[u].append((v, weight))
start, destination = map(int, input().split())


dist = [1005 * 100000] * (n + 1)
dist[start] = 0


Q = []
heapq.heappush(Q, (0, start))


while Q:
    dist_x, x = heapq.heappop(Q)


    if dist[x] != dist_x: continue


    for u, weight in con[x]:

        if dist[u] > dist[x] + weight:
            dist[u] = dist[x] + weight
            heapq.heappush(Q, (dist[u], u))

print(dist[destination])