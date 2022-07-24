"""
3273 두 수의 합
"""
import sys

input = sys.stdin.readline
n = int(input())
ls = sorted(map(int, input().split()))
target = int(input())
l, r = 0, n - 1
cnt = 0
while l < r:
    if ls[l] + ls[r] == target:
        cnt += 1
    if ls[l] + ls[r] >= target:
        r -= 1
    else:
        l += 1

print(cnt)
