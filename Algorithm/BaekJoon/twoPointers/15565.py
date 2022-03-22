"""

15565 귀여운 라이언

라이언 k개를 포함하는 가장 짧은 길이
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * 3
r = -1
ans = n + 1

for i in range(n):
    while r + 1 < n and cnt[1] < k:
        r += 1
        cnt[a[r]] += 1
    if cnt[1] >= k:
        ans = min(ans, r-i+1)
    cnt[a[i]] -= 1
if ans == n + 1:
    ans = -1

print(ans)