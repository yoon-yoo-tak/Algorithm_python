"""
2121 넷이 놀기
"""
import sys

input = sys.stdin.readline

def bisect(arr, l, r, k):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == k:
            return True
        if arr[mid] <= k:
            l = mid + 1
        else:
            r = mid - 1
    return False

n = int(input())
a, b = map(int, input().split())
ls = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0

for i in range(n):
    x, y = ls[i]
    if bisect(ls, 0, n - 1, [x + a, y]) and bisect(ls, 0, n - 1, [x, y + b]) and bisect(ls, 0, n - 1, [x + a, y + b]):
        ans += 1
print(ans)


