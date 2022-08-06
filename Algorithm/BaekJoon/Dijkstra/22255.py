"""
22255 호석사우루스
dist[x][y][k] := x, y 까지 k 번째 이동을 하여 올 수 있는 최소 충격량
"""
import sys, heapq
INF = int(1e10)
input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy, ex, ey = map(lambda x: x - 1, map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
dxy = [
    [(1, 0), (0, 1), (-1, 0), (0, -1)],  # 3K 번째 이동
    [(1, 0), (-1, 0)],                   # 3K + 1 번째 이동
    [(0, 1), (0, -1)]                    # 3K + 2 번째 이동
]
q = []
dist[sx][sy][1] = 0
heapq.heappush(q, (0, sx, sy, 1))
while q:
    dist_x, x, y, cnt = heapq.heappop(q)
    if dist_x != dist[x][y][cnt]:
        continue
    for dx, dy in dxy[cnt]:
        nx, ny, ncnt = x + dx, y + dy, (cnt + 1) % 3
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == -1:
            continue
        if dist[nx][ny][ncnt] > dist[x][y][cnt] + board[nx][ny]:
            dist[nx][ny][ncnt] = dist[x][y][cnt] + board[nx][ny]
            heapq.heappush(q, (dist[nx][ny][ncnt], nx, ny, ncnt))

print(-1 if min(dist[ex][ey]) == int(1e10) else min(dist[ex][ey]))