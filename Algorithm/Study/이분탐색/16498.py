"""
16498 작은 벌점
N ^ 3  >> 1초안에 안됨
N ^ 2 logN >> 가능
A, B 에서 고르는 모든 경우 + C에서 고르는 경우를 이분탐색
"""
import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline
a, b, c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(map(int, input().split()))
ans = int(1e9)
for i in A:
    for j in B:
        small = min(i, j)
        big = max(i, j)
        left = bisect_left(C, small)
        right = bisect_right(C, big)
        if left != right:
            ans = min(ans, big - small)
            continue
        if right != c:
            ans = min(ans, C[right] - small)
        if left != 0:
            ans = min(ans, big - C[left - 1])
print(ans)
