"""
14916 거스름돈
"""

import sys

input = sys.stdin.readline
dp = [0,-1,1,-1,2,1,3,2,4,3,2] + [0] * 100000

for i in range(11, 100001):
    dp[i] = min(dp[i - 2] + 1, dp[i - 5] + 1)

print(dp[int(input())])