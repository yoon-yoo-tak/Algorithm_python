"""
좌 상 우 하
"""
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
n = int(input())
d, x, y = 0, n - 1, n - 1
board = [[0] * n for _ in range(n)]
board[n - 1][n - 1] = n * n

while True:
    if board[x][y] == 1:
        break
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0:
        d = (d + 1) % 4
        continue
    board[nx][ny] = board[x][y] - 1
    x, y = nx, ny

for i in board:
    print(*i)