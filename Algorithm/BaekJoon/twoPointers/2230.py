"""

2230 수 고르기

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

r = 0
ans = 1 << 31

for i in range(n):
    while r + 1 < n and a[r] - a[i] < m:
        r += 1

    if a[r] - a[i] >= m:
        ans = min(ans, a[r] - a[i])

print(ans)
