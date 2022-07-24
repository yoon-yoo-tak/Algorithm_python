"""
2003 수들의 합
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ls = sorted(map(int, input().split()))
r, total, cnt = -1, 0, 0

for l in range(n):
    while r + 1 < n and total < m:
        r += 1
        total += ls[r]
    if total == m:
        cnt += 1
    total -= ls[l]

print(cnt)
