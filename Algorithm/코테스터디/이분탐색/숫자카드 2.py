"""
숫자카드 2
"""
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def upper_bound(a, l, r, x):
    idx = r + 1
    while l <= r:
        mid = (l + r) // 2
        # print('upper mid :', mid)
        if a[mid] > x:
            idx = mid
            r = mid - 1
        else:
            l = mid + 1
    return idx

def lower_bound(a, l, r, x):
    idx = r + 1
    while l <= r:
        mid = (l + r) // 2
        # print('lower mid :', mid)
        if a[mid] >= x:
            idx = mid
            r = mid - 1
        else:
            l = mid + 1
    return idx

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(a)
for x in b:
    print(upper_bound(a, 0, n - 1, x) - lower_bound(a, 0, n - 1, x), end=' ')


for x in b:
    print(bisect_right(a, x) - bisect_left(a, x), end=' ')