"""

1806 부분합

투포인터로 s이상이 될 때까지 r을 움직여줌 > s이상이면 l을 움직이면서 하나씩 빼줌

"""
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = n + 1
sum = 0
r = -1

for l in range(n):
    while r + 1 < n and sum < s:
        r += 1
        sum += a[r]

    if sum >= s:
        ans = min(ans, r - l + 1)
    sum -= a[l]

if ans == n + 1:
    ans = 0
print(ans)
