"""
15961 회전 초밥
"""
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
ls = [int(input()) for _ in range(n)]
temp = [0] * (d + 1)
curr = 1
temp[c] += 1

for i in range(k):
    temp[ls[i]] += 1
    if temp[ls[i]] == 1:
        curr += 1
ans = curr

for i in range(1, n):
    before = (i - 1) % n
    after = (i + k - 1) % n
    temp[ls[before]] -= 1
    if temp[ls[before]] < 1:
        curr -= 1
    temp[ls[after]] += 1
    if temp[ls[after]] == 1:
        curr += 1
    if ans < curr:
        ans = curr
print(ans)