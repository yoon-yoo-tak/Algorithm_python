"""
숫자 등장 횟수
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
nums = list(map(int, input().split()))
d = defaultdict(int)
for i in ls:
    d[i] += 1
for i in nums:
    print(d[i], end=' ')