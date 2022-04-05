"""
2565 전깃줄

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

n = int(input())
a = []
b = []
dp = [0] * n
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x:x[0])

for i in range(n):
    b.append(a[i][1])
for i in range(n):
    for j in range(i):
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))