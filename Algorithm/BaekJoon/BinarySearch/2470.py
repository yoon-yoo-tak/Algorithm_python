"""
2470 두 용액
이분탐색풀이
"""

import sys

input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))

def lower_bound(a, l, r, x):
    result = r + 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    return result


best = 1 << 31
v1, v2 = 0, 0
for i in range(n):
    res = lower_bound(a, i + 1, n - 1, -a[i])

    if i < res - 1 and abs(a[i] + a[res - 1]) < best:
        best = abs(a[i] + a[res - 1])
        v1, v2 = a[i], a[res - 1]

    if res < n and abs(a[i] + a[res]) < best:
        best = abs(a[i] + a[res])
        v1, v2 = a[i], a[res]

print(v1, v2)
