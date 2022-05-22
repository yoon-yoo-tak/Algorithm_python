import sys

input = sys.stdin.readline


def comf(x, y):
    cnt = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            cnt += 1
    return True if cnt == 3 else False

n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if comf(r, c):
        print(1)
    else:
        print(0)
    board[r][c] = 1
