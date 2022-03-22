"""

2512 에산

"""
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())

def ok(d):
    sum = 0
    for x in a:
        if x<=d:
            sum += x
        else:
            x = d
            sum += x
    return sum <= m

l = 1
r = 1000000000
ans = 0

if sum(a) > m:  # 요청 금액 합이 총 예산보다 클때만 수행해라
    while l <= r:
        mid = (l + r) // 2
        if ok(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
else: # 요청 금액 합이 총 예산보다 적으면 최대값이 상한이다.
    ans = sorted(a)[len(a)-1]

print(ans)
