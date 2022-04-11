"""
20291 파일 정리

"""

import sys

input = sys.stdin.readline
n = int(input())
h = dict()
for _ in range(n):
    a, b = input().split('.')

    if b not in h:
        h[b] = 1
    else:
        h[b] += 1

sorting = sorted(h.items())
for key, value in sorting:
    print(key.strip(), value)



