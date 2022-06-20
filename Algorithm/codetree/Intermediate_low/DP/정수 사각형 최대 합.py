"""
정수 사각형 최대 합
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = ls[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + ls[0][i]
    dp[i][0] = dp[i - 1][0] + ls[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j - 1] + ls[i][j], dp[i - 1][j] + ls[i][j])
print(dp[n - 1][n - 1])


