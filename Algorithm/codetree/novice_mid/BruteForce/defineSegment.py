"""
구간 중 최대 합
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))
ans = -1
for i in range(n - k + 1):
    ans = max(ans, sum(ls[i:i + k]))
print(ans)