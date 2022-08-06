"""
1654 랜선 자르기
"""
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ls = list(int(input()) for _ in range(k))
l, r = 0, max(ls)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if sum([i // mid for i in ls]) >= n:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
