"""
2473 세 용액
"""
import sys

input = sys.stdin.readline
n = int(input())
ls = sorted(map(int, input().split()))
best = int(1e10)


v1, v2, v3 = 0, 0, 0
for idx in range(n):
    l, r = 0, n - 1
    while l < r:
        if l == idx:
            l += 1
        elif r == idx:
            r -= 1
        else:
            curr = ls[idx] + ls[l] + ls[r]
            if abs(curr) < best:
                best = abs(curr)
                v1, v2, v3 = ls[idx], ls[l], ls[r]
            if curr > 0:
                r -= 1
            else:
                l += 1
print(v1, v2, v3)