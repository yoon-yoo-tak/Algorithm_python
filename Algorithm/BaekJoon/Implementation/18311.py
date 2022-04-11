"""
18311 왕복
"""

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
ls = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    ls[i] = ls[i] + ls[i - 1]
if k > max(ls):
    k = max(ls) - (k - max(ls))

for i in range(n):
    if ls[i] <= k < ls[i + 1]:
        ans = i + 1

print(ans)