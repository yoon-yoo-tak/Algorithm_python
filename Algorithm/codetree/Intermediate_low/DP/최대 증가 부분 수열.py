"""
최대 증가 부분 수열
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if ls[j] >= ls[i]:
            continue
        dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))