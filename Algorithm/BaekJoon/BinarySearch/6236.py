"""

6236 용돈 관리

인출금액 K원일때 M번 인출 할 수 있는가?

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

def ok(w):
    cnt, sum = 1, 0
    for x in a:
        if sum + x > w:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt <= m

l, r, ans = max(a), 1000000000, 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)