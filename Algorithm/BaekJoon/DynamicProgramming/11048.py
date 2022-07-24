"""
11048 이동하기
아래, 오른쪽, 오른쪽아래
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = board[0][0]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + board[i][0]
for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + board[0][i]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j] + board[i][j], dp[i][j - 1] + board[i][j], dp[i - 1][j - 1] + board[i][j])
print(dp[n - 1][m - 1])