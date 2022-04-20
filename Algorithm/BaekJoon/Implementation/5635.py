"""
5635 생일
"""

import sys

input = sys.stdin.readline
n = int(input())
ls = []
for _ in range(n):
    a, b, c, d = input().split()
    ls.append((a, int(b), int(c), int(d)))
ls.sort(key=lambda x:(x[3], x[2], x[1]))
print(ls[n - 1][0])
print(ls[0][0])
