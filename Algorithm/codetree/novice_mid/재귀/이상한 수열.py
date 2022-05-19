
import sys

input = sys.stdin.readline


def rec(k):
    if k <= 2:
        return k
    return rec(k // 3) + rec(k - 1)


n = int(input())

print(rec(n))