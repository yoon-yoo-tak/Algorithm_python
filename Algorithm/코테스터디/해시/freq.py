"""
빈도정렬
"""
import sys
from collections import defaultdict
input=sys.stdin.readline
A = defaultdict(int)

n, m = map(int, input().split())

data = list(map(int, input().split()))

for i in data:
    A[i] += 1

ans = sorted([[i, A[i]] for i in A], key=lambda x: (-x[1]))
for key, value in ans:
    for _ in range(value):
        print(key, end=' ')
