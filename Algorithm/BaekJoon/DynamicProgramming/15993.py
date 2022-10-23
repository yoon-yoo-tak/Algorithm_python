"""
1,2,3 더하기 8
"""
import sys
input = sys.stdin.readline
MOD = 1000000009

dp = [[0] * 100001 for _ in range(2)]
dp[0][1] = 1
dp[0][2], dp[1][2] = 1, 1
dp[0][3], dp[1][3] = 2, 2

for i in range(4, 100001):
    dp[0][i] = (dp[1][i - 1] + dp[1][i - 2] + dp[1][i - 3]) % MOD
    dp[1][i] = (dp[0][i - 1] + dp[0][i - 2] + dp[0][i - 3]) % MOD

for _ in range(int(input())):
    n = int(input())
    print(dp[0][n], dp[1][n])

