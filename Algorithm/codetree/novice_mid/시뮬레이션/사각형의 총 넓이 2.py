import sys

input = sys.stdin.readline

offset = 100

board = [[0] * 201 for _ in range(201)]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

ans = 0
for i in board:
    ans += sum(i)
print(ans)
