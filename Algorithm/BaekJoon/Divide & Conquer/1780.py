"""
1780 종이의 개수
"""
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

minus = 0
zero = 0
one = 0

def rec(x, y, k):
    global minus, zero, one

    check = board[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if (board[i][j] != check):
                for l in range(3):
                    for m in range(3):
                        rec(x + l * k // 3, y + m * k // 3, k // 3)
                return
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        one += 1

rec(0, 0, n)
print(minus)
print(zero)
print(one)