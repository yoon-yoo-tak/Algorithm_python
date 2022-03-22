"""

2110 공유기 설치


"""
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

def ok(D):
    cnt, last = 1, a[0]
    for i in range(1, n):
        if a[i] - last < D: continue
        last = a[i]
        cnt += 1
    return cnt >= c

l, r, ans = 1, 1000000000, 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
