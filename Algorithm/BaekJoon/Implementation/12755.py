"""
12755 수면 장애

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
n = int(input())
ls = []
i = 1
while len(ls) != n:
    s = str(i)
    for j in s:
        ls.append(j)
    i += 1
print(ls[n - 1])