"""
3231 카드놀이
"""

import sys

input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]
ans = 0
for i in range(1, n):
    if ls.index(i) > ls.index(i + 1):
        ans += 1
print(ans)

