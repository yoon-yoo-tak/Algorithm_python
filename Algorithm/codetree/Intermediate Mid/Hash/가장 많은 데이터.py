"""
가장 많은 데이터
"""
import sys
from collections import defaultdict
input = sys.stdin.readline
d = defaultdict(int)
for _ in range(int(input())):
    d[input().strip()] += 1
print(max(d.values()))