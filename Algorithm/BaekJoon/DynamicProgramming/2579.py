"""
2579 계단 오르기

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

dp = [[0, 0] for _ in range(n + 2)]

dp[0][0], dp[0][1] = 0, a[0]


if n >= 2:
    dp[1][0], dp[1][1] = a[1], a[0] + a[1]

for i in range(2, n):
    dp[i][0] = max(dp[i - 2][0] + a[i], dp[i - 2][1] + a[i])
    dp[i][1] = dp[i - 1][0] + a[i]

print(max(dp[n - 1][0], dp[n - 1][1]))

