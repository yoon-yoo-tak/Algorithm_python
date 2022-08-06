"""
13702 이상한 술집
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(int(input()) for _ in range(n))
l, r = 1, max(ls)
ans = 0
while l <= r:
    mid = (l + r) // 2
    total = sum([i // mid for i in ls])
    if total >= k:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
