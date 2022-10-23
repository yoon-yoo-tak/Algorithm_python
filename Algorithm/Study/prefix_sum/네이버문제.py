"""
5 2
5 3 6 1 3

=> 2

4 2
8 8 4 3

=> 0

6 4
3 5 1 3 9 8

=> 1
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
rev_a = a[::-1]
prefix_mx = [0] * n
prefix_mn = [0] * n
suffix_mx = [0] * n
suffix_mn = [0] * n

prefix_mx[0], prefix_mn[0] = a[0], a[0]
suffix_mx[0], suffix_mn[0] = a[-1], a[-1]

for i in range(1, n):
    prefix_mx[i] = max(prefix_mx[i - 1], a[i])
    prefix_mn[i] = min(prefix_mn[i - 1], a[i])

for i in range(1, n):
    suffix_mx[i] = max(suffix_mx[i - 1], rev_a[i])
    suffix_mn[i] = min(suffix_mn[i - 1], rev_a[i])
suffix_mn = suffix_mn[::-1]
suffix_mx = suffix_mx[::-1]

ans = int(1e9)

for i in range(n - k + 1):
    if i == 0:
        ans = min(ans, suffix_mx[i + k] - suffix_mn[i + k])
    elif i == n - k:
        ans = min(ans, prefix_mx[k - 1] - prefix_mn[k - 1])
    else:
        val = max(prefix_mx[i - 1], suffix_mx[i + k]) - min(prefix_mn[i - 1], suffix_mn[i + k])
        ans = min(ans, val)

print(ans)


