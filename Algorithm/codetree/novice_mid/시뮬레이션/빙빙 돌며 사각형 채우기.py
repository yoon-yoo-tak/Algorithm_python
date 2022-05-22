"""
우 하 좌 상
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d, x, y = 0, 0, 0
board = [[0] * m for _ in range(n)]
start = 65
board[x][y] = chr(start)
cnt = 1
while True:
    if cnt == n * m:
        break
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 0:
        d = (d + 1) % 4
        continue
    start = start + 1
    if start == 91:
        start = 65
    board[nx][ny] = chr(start)
    cnt += 1
    x, y = nx, ny

for i in board:
    print(*i)