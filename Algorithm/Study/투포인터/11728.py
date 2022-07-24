"""
11728 배열 합치기
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

l, r = 0, 0
while l < n and r < m:
    if a[l] < b[r]:
        print(a[l], end=' ')
        l += 1
    else:
        print(b[r], end=' ')
        r += 1
while l < n:
    print(a[l], end=' ')
    l += 1
while r < m:
    print(b[r], end=' ')
    r += 1