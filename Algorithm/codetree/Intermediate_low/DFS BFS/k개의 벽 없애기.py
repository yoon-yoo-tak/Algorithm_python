"""
k개의 벽 없애기
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append([x, y, 0, 0])
    visited[0][x][y] = 1
    while q:
        x, y, wall, dist = q.popleft()
        if x == ex and y == ey:
            return dist
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if board[nx][ny] == 1 and wall < K and not visited[wall + 1][nx][ny]:
                    q.append([nx, ny, wall + 1, dist + 1])
                    visited[wall + 1][nx][ny] = 1
                elif board[nx][ny] == 0 and not visited[wall][nx][ny]:
                    q.append([nx, ny, wall, dist + 1])
                    visited[wall][nx][ny] = 1
    return -1


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * N for _ in range(N)] for k in range(K + 1)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
sx, sy = map(lambda x: x - 1, map(int, input().split()))
ex, ey = map(lambda x: x - 1, map(int, input().split()))
print(bfs(sx, sy))