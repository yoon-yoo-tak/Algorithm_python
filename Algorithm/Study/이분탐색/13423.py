"""
13423 Three dots
N ^ 3 불가능
N ^ 2 까지 가능하다 >> 2개 정하고 하나 찾기
"""
import sys

input = sys.stdin.readline


def bisect(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
    return False


for _ in range(int(input())):
    n = int(input())
    dots = sorted(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ab = abs(dots[j] - dots[i])
            if bisect(dots, 0, n - 1, ab + dots[j]):
                ans += 1
    print(ans)