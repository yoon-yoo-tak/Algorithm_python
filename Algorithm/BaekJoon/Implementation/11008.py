"""
11008 복붙의 달인

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    a, b = input().split()
    if b in a:
        cnt += a.count(b)
        a = a.replace(b, '')
    cnt += len(a)
    print(cnt)