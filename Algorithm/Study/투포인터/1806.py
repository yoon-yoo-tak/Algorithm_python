"""
1806 부분 합
"""
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
ls = list(map(int, input().split()))
r, total, ans = -1, 0, n + 1
for l in range(n):
    while r + 1 < n and total < s:
        r += 1
        total += ls[r]
    if total >= s:
        ans = min(ans, r - l + 1)
    total -= ls[l]
print(ans if ans != n + 1 else 0)