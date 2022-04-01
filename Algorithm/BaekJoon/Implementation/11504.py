"""
11504 돌려 돌려 돌림판!
"""

import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = ''.join(input().split())
    y = ''.join(input().split())
    count = 0
    ls = input().split()
    for i in range(n):
        num = ''
        for j in range(m):
            num += ls[(i + j) % n]
        if x <= num <= y:
            count += 1
    print(count)
