"""

3273 두 수의 합


"""
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
S = int(input())
a.sort()
L, R, ans = 0, n - 1, 0
while L < R:
    if a[L] + a[R] == S:
        ans += 1
    if a[L] + a[R] >= S:
        R -= 1
    else:
        L += 1
print(ans)