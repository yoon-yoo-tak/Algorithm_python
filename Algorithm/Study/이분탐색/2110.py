"""
2110 공유기 설치
"""
import sys

input = sys.stdin.readline

def ok(x):
    cnt, last = 1, ls[0]
    for i in range(1, n):
        if ls[i] - last < x:
            continue
        last = ls[i]
        cnt += 1
    return cnt >= c


n, c = map(int, input().split())
ls = sorted(int(input()) for _ in range(n))

l, r, ans = 0, 1000000000, 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)