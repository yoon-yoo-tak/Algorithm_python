"""
2143 두 배열의 합
"""
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def upper_bound(a, l, r, x):
    idx = r + 1
    while l <= r:
        mid = (l + r) // 2
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
        if a[mid] >= x:
            idx = mid
            r = mid - 1
        else:
            l = mid + 1
    return idx


t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
prefix_a = []
prefix_b = []

for i in range(n): # 누적합
    total = 0
    for j in range(i, n):
        total += a[j]
        prefix_a.append(total)
for i in range(m): # 누적합
    total = 0
    for j in range(i, m):
        total += b[j]
        prefix_b.append(total)

cnt = 0
prefix_b.sort() # b에서 찾을거니까 정렬
for i in prefix_a:
    target = t - i
    lower_idx = lower_bound(prefix_b, 0, len(prefix_b) - 1, target)
    if lower_idx >= len(prefix_b):
        continue
    upper_idx = upper_bound(prefix_b, 0, len(prefix_b) - 1, target)
    if prefix_b[lower_idx] == target:
        cnt += upper_idx - lower_idx
print(cnt)