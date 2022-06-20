"""

1806 부분합

투포인터로 s이상이 될 때까지 r을 움직여줌 > s이상이면 l을 움직이면서 하나씩 빼줌

"""
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
ls = list(map(int, input().split()))
total, r = 0, -1
ans = n + 1
for l in range(n):
    while r + 1 < n and total < s:
        r += 1
        total += ls[r]

    if total >= s:
        ans = min(ans, r - l + 1)

    total -= ls[l]

print(ans if ans != n + 1 else 0)