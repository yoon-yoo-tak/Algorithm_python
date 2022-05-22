import sys

input = sys.stdin.readline

# 아래, 오른, 위 ,왼

n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = [[0] * m for _ in range(n)]
x, y = 0, 0
dir = 0
board[x][y] = 1
while True:
    if board[x][y] == n * m:
        break
    nx, ny = x + dx[dir], y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 0:
        dir = (dir + 1) % 4
        continue
    board[nx][ny] = board[x][y] + 1
    x, y = nx, ny
for i in board:
    print(*i)