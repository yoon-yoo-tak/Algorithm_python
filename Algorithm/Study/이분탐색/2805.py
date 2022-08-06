"""
2805 나무 자르기
"""
import sys

input = sys.stdin.readline


def ok(h):
    total = 0
    for i in trees:
        if i >= h:
            total += i - h
    return total >= m

n, m = map(int, input().split())
trees = list(map(int, input().split()))
ans = 0
l, r = 0, max(trees)
while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
