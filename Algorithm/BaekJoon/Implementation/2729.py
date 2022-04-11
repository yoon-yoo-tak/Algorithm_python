"""
2729 이진수 덧셈
"""

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    print(bin((a + b))[2:])

