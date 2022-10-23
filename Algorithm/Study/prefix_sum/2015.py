"""
2015 수들의 합 4
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0
prefix_sum = defaultdict(int)

for i in range(1, n):
    ls[i] += ls[i - 1]
for i in range(n):
    if ls[i] == k:
        cnt += 1
    cnt += prefix_sum[ls[i] - k]
    prefix_sum[ls[i]] += 1
print(cnt)

