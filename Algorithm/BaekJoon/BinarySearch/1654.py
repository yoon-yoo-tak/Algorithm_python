"""

1654 랜선 자르기

"""
import sys
input = sys.stdin.readline

k, n = map(int, input().split())

a = [int(input()) for _ in range(k)]

def ok(d):
    sum = 0
    for x in a:
        sum += x // d
    return sum >= n

l = 1
r = 1 << 31
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)