"""
2792 보석 상자
"""
import sys, math

input = sys.stdin.readline

def bisect(l, r):
    ans = int(1e10)
    while l <= r:
        mid = (l + r) // 2
        temp = 0
        for i in ls:
            temp += math.ceil(i / mid)
        if temp > n:
            l = mid + 1
        else:
            r = mid - 1
            ans = min(ans, mid)
    return ans


n, m = map(int, input().split())
ls = list(int(input()) for _ in range(m))
print(bisect(1, max(ls)))