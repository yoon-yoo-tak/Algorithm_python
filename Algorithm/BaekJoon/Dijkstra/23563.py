"""
23563 벽 타기
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def check(x, y):
    cnt = 0
    for dx, dy in dxy:
        if graph[x + dx][y + dy] == '#':
            cnt += 1
    return True if cnt > 0 else False

def dijkstra(sx, sy, ex, ey):
    dist = [[INF] * m for _ in range(n)]
    q = []
    heapq.heappush(q, (0, sx, sy))
    dist[sx][sy] = 0
    while q:
        dist_x, x, y = heapq.heappop(q)
        if dist[x][y] != dist_x:
            continue
        is_wall = check(x, y)
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#':
                continue
            next_is_wall = check(nx, ny)
            if is_wall and next_is_wall:
                if dist[nx][ny] > dist[x][y]:
                    dist[nx][ny] = dist[x][y]
                    heapq.heappush(q, (dist[nx][ny], nx, ny))
            else:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    heapq.heappush(q, (dist[nx][ny], nx, ny))
    return dist[ex][ey]



n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            sx, sy = i, j
        elif graph[i][j] == 'E':
            ex, ey = i, j


print(dijkstra(sx, sy, ex, ey))