"""
22116 창영이와 퇴근
"""
import sys, heapq

input = sys.stdin.readline

n = int(input())
graph =[list(map(int, input().split())) for _ in range(n)]
dist = [[int(1e11)] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = []
dist[0][0] = 0
heapq.heappush(q, (0, 0, 0))
while q:
    dist_xy, x, y = heapq.heappop(q)
    if dist[x][y] != dist_xy:
        continue
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if dist[nx][ny] > max(dist_xy, abs(graph[x][y] - graph[nx][ny])):
            dist[nx][ny] = max(dist_xy, abs(graph[x][y] - graph[nx][ny]))
            heapq.heappush(q, (dist[nx][ny], nx, ny))

print(dist[n - 1][n - 1])

