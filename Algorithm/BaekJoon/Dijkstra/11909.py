"""
11909 배열 탈출
"""
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
dxy = [(1, 0), (0, 1)]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[INF] * n for _ in range(n)]

q = []
heapq.heappush(q, (0, 0, 0))
dist[0][0] = 0
while q:
    dist_x, x, y = heapq.heappop(q)
    if dist_x != dist[x][y]:
        continue
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][nx] < board[x][y]:
            if dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                heapq.heappush(q, (dist[nx][ny], nx, ny))
        elif board[nx][ny] >= board[x][y]:
            if dist[nx][ny] > dist[x][y] + abs(board[nx][ny] - board[x][y]) + 1:
                dist[nx][ny] = dist[x][y] + abs(board[nx][ny] - board[x][y]) + 1
                heapq.heappush(q, (dist[nx][ny], nx, ny))
        for i in dist:
            print(i)
        print()
print(dist[n - 1][n - 1])