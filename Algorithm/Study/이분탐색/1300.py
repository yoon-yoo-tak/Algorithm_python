"""
1300 K번째 수
"""
import sys

input = sys.stdin.readline

def ok(x):
    total = 0
    for i in range(1, n + 1):
        total += min(n, x // i)
    return total >= k


n = int(input())
k = int(input())
l, r, ans = 1, n * n, 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)