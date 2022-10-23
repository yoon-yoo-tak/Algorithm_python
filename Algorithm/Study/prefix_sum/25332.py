"""
25332 수들의 합 8
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + b[i - 1] - a[i - 1]
ans = 0
cnt = defaultdict(int)
for i in range(1, n + 1):
    if prefix_sum[i] == 0:
        ans += 1
    ans += cnt[prefix_sum[i]]
    cnt[prefix_sum[i]] += 1
print(ans)