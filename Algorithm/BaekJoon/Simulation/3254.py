"""
3254 김밥 21개
"""

import sys

input = sys.stdin.readline
# 상근 1 정인 2


def throw_drop(s, j):
    for i in range(6):
        if board[i][s - 1] == 0:
            board[i][s - 1] = 1
            break
    for i in range(6):
        if board[i][j - 1] == 0:
            board[i][j - 1] = 2
            break


def check():
    for i in range(6):
        for j in range(7):
            if board[i][j] == 1:
                cnt = 1
                x, y = i, j
                while True:
                    nx, ny = x, y + 1
                    if y >= 7:
                        break
                    if board[nx][ny] != 1:
                        break
                    cnt += 1
                    x, y = nx , ny
                if cnt >= 4:
                    return 'sk'
                cnt = 1
                x, y = i, j
                while True:
                    nx, ny = x + 1, y
                    if x >= 7:
                        break
                    if board[nx][ny] != 1:
                        break
                    cnt += 1
                    x, y = nx, ny
                if cnt >= 4:
                    return 'sk'
                cnt = 1
                x, y = i, j
                while True:
                    nx, ny = x + 1, y + 1
                    if y >= 7 or x >= 6:
                        break
                    if board[nx][ny] != 1:
                        break
                    cnt += 1
                    x, y = nx, ny
                if cnt >= 4:
                    return 'sk'
            elif board[i][j] == 2:
                cnt = 1
                x, y = i, j
                while True:
                    nx, ny = x, y + 1
                    if y >= 7:
                        break
                    if board[nx][ny] != 2:
                        break
                    cnt += 1
                    x, y = nx, ny
                if cnt >= 4:
                    return 'ji'
                cnt = 1
                x, y = i, j
                while True:
                    nx, ny = x + 1, y
                    if x >= 7:
                        break
                    if board[nx][ny] != 2:
                        break
                    cnt += 1
                    x, y = nx, ny
                if cnt >= 4:
                    return 'ji'
                cnt = 1
                x, y = i, j
                while True:
                    nx, ny = x + 1, y + 1
                    if y >= 7 or x >= 6:
                        break
                    if board[nx][ny] != 2:
                        break
                    cnt += 1
                    x, y = nx, ny
                if cnt >= 4:
                    return 'ji'
    return 'ss'

board = [[0] * 7 for _ in range(6)]
turn = []
for _ in range(21):
    a, b = map(int, input().split())
    turn.append([a, b])

for i in range(4):
    throw_drop(turn[i][0], turn[i][1])
idx = 1
for x, y in turn:
    throw_drop(x, y)
    ans = check()
    if ans != 'ss':
        print(ans, idx)
        break
    idx += 1

