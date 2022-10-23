"""
2143 두 배열의 합
"""
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


# def upper_bound(ls: list, l: int, r: int, x: int) -> int:
#     idx = r + 1
#     while l <= r:
#         mid = (l + r) // 2
#         if ls[mid]> x:
#             idx = mid
#             r = mid - 1
#         else:
#             l = mid + 1
#     return idx
#
#
# def lower_bound(ls: list, l: int, r: int, x: int) -> int:
#     idx = r + 1
#     while l <= r:
#         mid = (l + r) // 2
#         if ls[mid] >= x:
#             idx = mid
#             r = mid -1
#         else:
#             l = mid + 1
#     return idx

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

prefix_sum_a = []
prefix_sum_b = []

for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        prefix_sum_a.append(temp)

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        prefix_sum_b.append(temp)

ans = 0
prefix_sum_b.sort()
for i in prefix_sum_a:
    target = t - i
    # l_bound = lower_bound(prefix_sum_b, 0, len(prefix_sum_b) - 1, target)
    l_bound = bisect_left(prefix_sum_b, target)
    # u_bound = upper_bound(prefix_sum_b, 0, len(prefix_sum_b) - 1, target)
    u_bound = bisect_right(prefix_sum_b, target)
    if l_bound >= len(prefix_sum_b):
        continue
    if prefix_sum_b[l_bound] == target:
        ans += u_bound - l_bound
print(ans)