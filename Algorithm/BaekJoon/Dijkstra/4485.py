"""
4485 녹색 옷 입은 애가 젤다지?
"""
import sys, heapq
INF = int(1e9)
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
tt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]
    while q:
        dist_x, x, y = heapq.heappop(q)
        if dist[x][y] != dist_x:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] > dist[x][y] + graph[nx][ny]:
                dist[nx][ny] = dist[x][y] + graph[nx][ny]
                heapq.heappush(q, (dist[nx][ny], nx, ny))
    print(f'Problem {tt}: {dist[n - 1][n - 1]}')
    tt += 1