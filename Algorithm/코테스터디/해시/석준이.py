"""
걸그룹 마스터 석준이
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

girl = defaultdict(list)
for _ in range(n):
    group_name = input().strip()
    for _ in range(int(input())):
        girl[group_name].append(input().strip())

for _ in range(m):
    name = input().strip()
    num = int(input())
    if num:
        for key, value in girl.items():
            if name in value:
                print(key)
                break
    else:
        for i in sorted([memeber for memeber in girl[name]]):
            print(i)