"""
10295 Hiking
"""
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for _ in range(int(input())):
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    start_x, start_y = map(int, input().split())
    height = 0
    end_x, end_y = -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j].isdigit():
                if int(board[i][j]) > height:
                    height = int(board[i][j])
                    end_x, end_y = i, j
    dist = [[INF] * m for _ in range(n)]
    q = []
    heapq.heappush(q, (0, start_x, start_y))
    dist[start_x][start_y] = 0
    while q:
        dist_x, x, y = heapq.heappop(q)
        if dist_x != dist[x][y]:
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == '#':
                continue
            if int(board[nx][ny]) == int(board[x][y]):
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    heapq.heappush(q, (dist[nx][ny], nx, ny))
            else:
                diff = int((abs(int(board[nx][ny]) - int(board[x][y])) + 1) ** 2)
                if dist[nx][ny] > dist[x][y] + diff:
                    dist[nx][ny] = dist[x][y] + diff
                    heapq.heappush(q, (dist[nx][ny], nx, ny))
    print(dist[end_x][end_y] if dist[end_x][end_y] != int(1e9) else 'NO')

