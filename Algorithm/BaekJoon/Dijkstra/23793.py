import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
x, y, z = map(int, input().split())

def Dijkstra(start, flag= True):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    if flag:
        while q:
            dist_x, xx = heapq.heappop(q)
            if dist[xx] < dist_x: continue

            for u, weight in graph[xx]:
                if dist[u] > dist_x + weight:
                    dist[u] = dist_x + weight
                    heapq.heappush(q, (dist[u], u))
    else:
        while q:
            dist_x, xx = heapq.heappop(q)
            if dist[xx] < dist_x: continue

            for u, weight in graph[xx]:
                if u == y: continue
                if dist[u] > dist_x + weight:
                    dist[u] = dist_x + weight
                    heapq.heappush(q, (dist[u], u))
    return dist

distances_1 = Dijkstra(x, True)
distances_2 = Dijkstra(y, True)
distances_3 = Dijkstra(x, False)

answer1 = distances_1[y] + distances_2[z]
answer2 = distances_3[z]

print(-1 if answer1 >= INF else answer1, end=' ')
print(answer2 if answer2 != INF else -1)
