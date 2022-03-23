"""

13706 제곱근

N이 주어졌을때 N의 제곱근을 구하기.

"""
import sys
input = sys.stdin.readline

n = int(input())
l = 1
r = n
while l <= r:
    mid = (l + r) // 2
    if mid ** 2 == n:
        print(mid)
        break
    if mid ** 2 < n:
        l = mid + 1
    else:
        r = mid - 1


