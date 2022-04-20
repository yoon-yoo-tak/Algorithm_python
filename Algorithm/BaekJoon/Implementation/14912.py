"""
14912 숫자 빈도수
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = []
for i in range(1, n + 1):
    while i > 0:
        ls.append(i % 10)
        i //= 10
print(ls.count(m))
