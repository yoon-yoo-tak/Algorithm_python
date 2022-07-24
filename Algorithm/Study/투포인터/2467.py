"""
2467 용액
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
best = int(1e10)
v1, v2, l, r = 0, 0, 0, n - 1

while l < r:
    total = ls[l] + ls[r]
    if abs(total) < best:
        best = abs(total)
        v1 = ls[l]
        v2 = ls[r]
    if total > 0:
        r -= 1
    else:
        l += 1
print(v1, v2)