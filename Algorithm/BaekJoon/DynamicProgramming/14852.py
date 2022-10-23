"""
14852 타일 채우기 3
"""
import sys

dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 7
n = int(input())
total = 0
for i in range(2, 1000001):
    total += dp[i - 3]
    dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2] + 2 * total) % 1000000007
print(dp[n])