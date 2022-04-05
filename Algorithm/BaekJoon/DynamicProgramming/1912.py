"""
1912 연속합

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
dp = [0] * len(ls)
dp[0] = ls[0]

for i in range(1, len(ls)):
    dp[i] = max(ls[i], dp[i - 1] + ls[i])

print(max(dp))