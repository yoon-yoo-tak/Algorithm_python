"""
2491 수열

"""

import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp, dp1 = [1] * n, [1] * n
for i in range(1, n):
    if ls[i] <= ls[i - 1]:
        dp[i] = max(dp[i], dp[i - 1] + 1)
    if ls[i] >= ls[i - 1]:
        dp1[i] = max(dp1[i], dp1[i - 1] + 1)
print(max(max(dp), max(dp1)))

