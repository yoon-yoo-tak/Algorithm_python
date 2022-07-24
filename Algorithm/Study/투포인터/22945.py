"""
22945 팀 빌딩
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
l, r, ans = 0, n - 1, 0

while l <= r:
    ans = max(ans, (r - l - 1) * min(ls[l], ls[r]))
    if ls[l] >= ls[r]:
        r -= 1
    else:
        l +=1
print(ans)

