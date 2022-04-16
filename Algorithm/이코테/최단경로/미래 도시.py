"""
이코테 최단경로 연습문제 1. 미래 도시
1에서 출발하여 k 를 거쳐 x 로 가는 최단시간
플로이드 활용
"""
import sys
INF = 1e9
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
distance = graph[1][k] + graph[k][x]

print(-1 if distance >= INF else distance)