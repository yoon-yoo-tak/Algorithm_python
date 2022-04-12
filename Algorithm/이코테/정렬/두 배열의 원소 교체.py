"""
두 배열의 원소 교체
"""

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()),reverse=True)
cnt = 0
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))


