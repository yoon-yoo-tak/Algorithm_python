"""
서로 다른 BST갯수 세기
"""
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 20

dp[0], dp[1] = 1, 1
dp[2] = 2
for i in range(3, 20):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[n])