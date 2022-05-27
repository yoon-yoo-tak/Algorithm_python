"""
최고의 33위치
"""
import sys

input = sys.stdin.readline


def check(x, y):
    total = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            total += board[i][j]
    return total

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 3 + 1):
    for j in range(n - 3 + 1):
        ans = max(ans, check(i, j))
print(ans)