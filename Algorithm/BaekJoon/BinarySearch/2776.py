"""

2776 암기왕

"""
import sys
input = sys.stdin.readline

def bise(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

t = int(input())

for i in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    for x in b:
        print(1 if bise(a, 0, n - 1, x) else 0)


