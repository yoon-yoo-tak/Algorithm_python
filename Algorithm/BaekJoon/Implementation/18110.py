"""
18110 solved.ac
"""

import sys

input = sys.stdin.readline


def new_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(input())
if n:
    arr = sorted(int(input()) for _ in range(n))
    nn = new_round(n * 0.15)
    print(new_round(sum(arr[nn:-nn] if nn else arr) / (n - 2 * nn)))
else:
    print(0)