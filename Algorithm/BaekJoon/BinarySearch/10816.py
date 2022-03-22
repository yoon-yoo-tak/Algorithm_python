"""

10816 숫자 카드 2

크기 N의 배열에 크기 M의 배열 원소가 몇개 있는지

이분탐색
"""
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def lower(a, l, r, x):
    res = r + 1
    while l<=r:
        mid = (l + r) // 2
        if a[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def upper(a, l, r, x):
    res = r + 1
    while l<=r:
        mid = (l + r) // 2
        if a[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

for x in b:
    print(upper(a, 0, n-1, x) - lower(a, 0, n-1, x), end=' ')
