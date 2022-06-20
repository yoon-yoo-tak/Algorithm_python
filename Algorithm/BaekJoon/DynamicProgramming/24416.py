"""
24416 알고리즘 수업 - 피보나치 수 1
"""
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 41
dp[1], dp[2] = 1, 1
for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n], n - 2)
