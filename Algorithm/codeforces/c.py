"""

"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    _ = input().strip()
    board = [list(input().strip()) for _ in range(8)]
    dxy = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                cnt = 0
                for dx, dy in dxy:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                        continue
                    if board[nx][ny] == '#':
                        cnt += 1
                if cnt == 4:
                    ans_x, ans_y = i + 1, j + 1
    print(ans_x, ans_y)
