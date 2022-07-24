"""
수 찾기
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


def bisect(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False


for x in b:
    print(1 if bisect(ls, 0, n - 1, x) else 0)