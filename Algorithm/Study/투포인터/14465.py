"""
14465 소가 길을 건너간 이유 5
"""
import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())
sign = [i for i in range(1, n + 1)]

for i in range(b):
    sign[int(input()) - 1] = 0

ans = 0
for i in range(k):
    if not sign[i]:
        ans += 1
temp = ans
for i in range(1, n - k + 1):
    if not sign[i - 1]:
        temp -= 1
    if not sign[i + k - 1]:
        temp += 1
    ans = min(ans, temp)
print(ans)