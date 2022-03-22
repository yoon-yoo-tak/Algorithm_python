"""

2003 수들의 합

i 부터 j까지의 합이 M이 되는 경우의 수

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

r, sum, cnt = -1, 0, 0

for l in range(n):
    while r + 1 < n and sum < m:
        r += 1
        sum += a[r]

    if sum == m:
        cnt += 1

    sum -= a[l]

print(cnt)
