"""
십자 모양 폭발
"""
import sys

input = sys.stdin.readline


def explode(x, y, size):
    temp_x = x
    while True:
        temp_x += 1
        if temp_x >= n or temp_x < 0:
            break
        if abs(x - temp_x) == size:
            break
        board[temp_x][y] = 0
    temp_x = x
    while True:
        temp_x -= 1
        if temp_x >= n or temp_x < 0:
            break
        if abs(x - temp_x) == size:
            break
        board[temp_x][y] = 0
    temp_y = y
    while True:
        temp_y += 1
        if temp_y >= n or temp_y < 0:
            break
        if abs(y - temp_y) == size:
            break
        board[x][temp_y] = 0
    temp_y = y
    while True:
        temp_y -= 1
        if temp_y >= n or temp_y < 0:
            break
        if abs(y - temp_y) == size:
            break
        board[x][temp_y] = 0

def extract(col):
    lst = []
    for i in range(n):
        lst.append(board[i][col])
    return lst


def pushing(ls):
    last = len(ls)
    for i in range(len(ls) - 1, -1, -1):
        if ls[i] == 0:
            continue
        last -= 1
        ls[last] = ls[i]
    for i in range(last - 1, -1, -1):
        ls[i] = 0
    return ls



def gravity():
    for i in range(n):
        temp_lst = extract(i)
        temp_lst = pushing(temp_lst)
        for j in range(n):
            board[j][i] = temp_lst[j]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda x: x - 1, map(int, input().split()))
length = board[r][c]
board[r][c] = 0
explode(r, c, length)
gravity()
for i in board:
    print(*i)
