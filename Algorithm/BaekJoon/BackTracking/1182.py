"""
1182 부분수열의 합
"""

import sys

input = sys.stdin.readline


def rec(k, val):
    global ans
    if k == n:
        if val == s:
            ans += 1
    else:
        rec(k + 1, val + nums[k])
        rec(k + 1, val)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
rec(0, 0)
if s == 0:
    ans -= 1
print(ans)
