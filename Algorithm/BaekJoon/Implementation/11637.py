"""
11637 인기 투표
"""

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m = int(input())
    ls = [int(input()) for _ in range(m)]
    max_val = max(ls)
    total = sum(ls)
    if ls.count(max_val) > 1:
        print('no winner')
        continue
    else:
        max_idx = ls.index(max_val) + 1
        if total // 2 < max_val:
            print(f'majority winner {max_idx}')
        else:
            print(f'minority winner {max_idx}')

