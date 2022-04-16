"""
이코테 최단경로 연습문제 화성탐사
"""
import sys, heapq
INF = int(1e9)
input = sys.stdin.readline

t = int(input())
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    for i in distance:
        print(*i)
