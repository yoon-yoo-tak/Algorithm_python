"""

2470 두 용액

합이 0에 가장 가깝게 고르기

"""
import sys
input = sys.stdin.readline

n = int(input())

a = sorted(map(int, input().split()))

best = 1e11
v1, v2, l, r = 0, 0, 0, n-1

while l < r:
    sum = a[l] + a[r]
    if (abs(sum) < best):
        best = abs(sum)
        v1 = a[l]
        v2 = a[r]

    if sum > 0:
        r -= 1
    else:
        l += 1

print(v1,v2)