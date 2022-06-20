"""

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

selected = [0] * m
def rec(x):
    if x == m:
        print(*selected)
        return
    else:
        for i in range(1, n + 1):
            selected[x] = i
            rec(x + 1)
            selected[x] = 0

rec(0)