"""
10816 두 수의 합
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
x = int(input())

ans = 0

def bisect(a, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == target:
            return True
        if a[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


for i in range(n):
    if bisect(ls, i + 1, n - 1, x - ls[i]):
        ans += 1

print(ans)