"""
11053 가장 긴 증가하는 부분 수열

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if ls[i] > ls[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(dp)
print(max(dp))