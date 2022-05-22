"""
오목
"""
import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]


def in_range(x, y):
    return  0 <= x < 19 and 0 <= y < 19


dx, dy = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]
dxy = [(1, -1), (1, 0), (1, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1)]

for i in range(19):
    for j in range(19):

        if board[i][j] == 0:
            continue
        for dx, dy in dxy:
            cnt = 1
            px, py = i, j
            while True:
                nx, ny = px + dx, py + dy
                if not in_range(nx, ny):
                    break
                if board[nx][ny] != board[i][j]:
                    break
                cnt += 1
                px, py = nx, ny

            if cnt == 5:
                print(board[i][j])
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                sys.exit()

print(0)
