"""
1149 RGB 거리

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]


for i in range(1, n + 1):
    a = list(map(int, input().split()))
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a[0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + a[1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + a[2]

print(min(dp[n]))