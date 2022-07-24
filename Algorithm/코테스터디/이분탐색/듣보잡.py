"""
듣보잡 이분탐색
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
listen = list(input().strip() for _ in range(n))
meet = sorted(input().strip() for _ in range(m))
ans = []

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

for x in listen:
    if bisect(meet, 0, m - 1, x):
        ans.append(x)
print(len(ans))
for i in sorted(ans):
    print(i)