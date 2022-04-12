"""
국영수
백준 10825
"""

import sys

input = sys.stdin.readline
n = int(input())
ls = []
for _ in range(n):
    a, b, c, d = input().split()
    ls.append([a, int(b), int(c), int(d)])

ls.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in ls:
    print(i[0])