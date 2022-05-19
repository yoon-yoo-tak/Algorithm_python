"""
반복 출력하기 2
"""

import sys

input = sys.stdin.readline


def rec(k):
    if k == 0:
        return
    rec(k - 1)
    print('HelloWorld')


n = int(input())
rec(n)