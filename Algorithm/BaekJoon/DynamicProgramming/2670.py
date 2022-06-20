"""
연속부분최대곱
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = [float(input()) for _ in range(n)]
dp = [0.0] * n

dp[0] = ls[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] * ls[i], ls[i])

print(f'{max(dp):.3f}')
