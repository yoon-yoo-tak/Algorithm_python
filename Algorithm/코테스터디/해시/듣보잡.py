"""
듣보잡
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

person = defaultdict(int)

for _ in range(n + m):
    person[input().strip()] += 1

name_lst = [name for name in person if person[name] == 2]

print(len(name_lst))
for i in sorted(name_lst):
    print(i)

